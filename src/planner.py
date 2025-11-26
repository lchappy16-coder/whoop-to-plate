import random
from src.models import WeeklyMetrics, WeeklyPlan, DayPlan, MealSlot, Recipe
from src.config import RECIPE_VAULT

class MealPlanner:
    def generate_precision_week(self, metrics: WeeklyMetrics, goal: str) -> WeeklyPlan:
        daily_plans = []
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        offset = 0
        if goal == "Lose 1 lb/week": offset = -500
        elif goal == "Gain 1 lb/week": offset = 500
        
        total_week_cals = 0

        for day in days:
            profile = metrics.weekday_profiles.get(day)
            if not profile: continue

            # Baseline Target
            daily_target = metrics.avg_daily_burn + offset
            if profile.avg_strain > 14: daily_target += 200 
            elif profile.avg_strain < 8: daily_target -= 200
            if daily_target < 1400: daily_target = 1400

            # Build Schedule
            schedule = self._build_daily_schedule(profile, int(daily_target))
            
            # Sum exact calories from the ROUNDED recipes
            exact_total = sum(s.recipe.calories for s in schedule)
            total_week_cals += exact_total

            daily_plans.append(DayPlan(day_name=day, target_calories=exact_total, schedule=schedule))
        
        avg_intake = int(total_week_cals / 7)
        return WeeklyPlan(
            summary=f"Goal: {goal}. Avg Intake: {avg_intake} kcal vs Burn: {metrics.avg_daily_burn} kcal.",
            daily_plans=daily_plans
        )

    def _build_daily_schedule(self, profile, total_budget_cals) -> list:
        slots = []
        is_workout_day = profile.avg_workout_time != "Rest Day"
        
        try: wake_h = int(profile.avg_wake_time.split(":")[0])
        except: wake_h = 7
        
        workout_h = 17 
        if is_workout_day:
            try: workout_h = int(profile.avg_workout_time.split(":")[0])
            except: workout_h = 17

        remaining_cals = total_budget_cals
        
        # Snack Allocation
        needs_snack = False
        snack_cals = 0
        if is_workout_day and workout_h > 12:
            needs_snack = True
            snack_cals = 250
            remaining_cals -= snack_cals

        # Meal Allocation (35/30/35 split of remainder)
        m1_cals = int(remaining_cals * 0.35)
        m2_cals = int(remaining_cals * 0.30)
        m3_cals = remaining_cals - m1_cals - m2_cals

        # Meal 1
        m1_h = wake_h + 1
        if is_workout_day and workout_h <= wake_h + 1: m1_h = workout_h + 1
        cat = "breakfast_high_fat"
        if is_workout_day and workout_h < 12: cat = "breakfast_high_carb"
        
        slots.append(MealSlot(self._fmt_time(m1_h), "Meal 1 (Break-Fast)", self._get_scaled_recipe(cat, m1_cals), "Satiety & Focus"))

        # Meal 2
        m2_h = m1_h + 4
        slots.append(MealSlot(self._fmt_time(m2_h), "Meal 2 (Lunch)", self._get_scaled_recipe("lunch_light", m2_cals), "Sustained Energy"))

        # Snack
        if needs_snack:
            snack_h = workout_h - 1
            if snack_h > m2_h + 1:
                slots.append(MealSlot(self._fmt_time(snack_h), "Pre-Workout Fuel", self._get_scaled_recipe("snacks", snack_cals), "Quick Glycogen"))

        # Meal 3
        m3_h = 18
        if is_workout_day and workout_h >= 17: m3_h = workout_h + 1
        if m3_h > 20: m3_h = 20
        if m3_h <= m2_h: m3_h = m2_h + 3
        slots.append(MealSlot(self._fmt_time(m3_h), "Meal 3 (Dinner)", self._get_scaled_recipe("dinner_recovery", m3_cals), "Deep Recovery"))

        return slots

    def _fmt_time(self, hour: int) -> str:
        if hour >= 24: hour -= 24
        suffix = "AM"
        disp = hour
        if hour >= 12:
            suffix = "PM"
            if hour > 12: disp -= 12
        elif hour == 0: disp = 12
        return f"{disp}:00 {suffix}"

    def _get_scaled_recipe(self, category, target_cals) -> Recipe:
        template = random.choice(RECIPE_VAULT[category])
        
        # 1. Get Base Nutrition
        base_cals = template.get('base_cals', 500)
        base_p = template.get('p', 20)
        base_f = template.get('f', 20)
        base_c = template.get('c', 20)
        
        # 2. Calculate Ratio
        raw_ratio = target_cals / base_cals
        
        # 3. ROUND TO NEAREST WHOLE NUMBER (Servings)
        # Max(1, ...) ensures we never tell the user to eat 0 servings
        servings = max(1, round(raw_ratio))
        
        # 4. Recalculate Macros based on the ROUNDED serving
        # This ensures the display matches reality (e.g. 2 servings = exactly 2x macros)
        final_cals = int(base_cals * servings)
        p = int(base_p * servings)
        f = int(base_f * servings)
        c = int(base_c * servings)
        
        return Recipe(
            title=template['title'] + f" ({servings} Servings)",
            description=template['desc'],
            ingredients_text=f"Portion scaled to {servings} servings",
            macros=f"{p}g P | {f}g F | {c}g C",
            calories=final_cals, # Use the recalculated calories
            search_query=template['query']
        )
