import random
from src.models import WeeklyMetrics, WeeklyPlan, DayPlan, MealSlot, Recipe
from src.config import RECIPE_VAULT

class MealPlanner:
    def generate_precision_week(self, metrics: WeeklyMetrics, goal: str) -> WeeklyPlan:
        daily_plans = []
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # 1. DETERMINE BASELINE OFFSET
        offset = 0
        if goal == "Lose 1 lb/week":
            offset = -500
        elif goal == "Gain 1 lb/week":
            offset = 500
        
        # Calculate Weekly Stats for Summary
        total_week_cals = 0

        for day in days:
            profile = metrics.weekday_profiles.get(day)
            if not profile: continue

            # 2. CALORIE MATH
            # Start with Daily Burn + Goal Offset
            daily_target = metrics.avg_daily_burn + offset

            # 3. STRAIN MICRO-ADJUSTMENTS
            # Even in a deficit, we fuel the work. Even in surplus, we cut back on rest days.
            if profile.avg_strain > 14: 
                daily_target += 200 
            elif profile.avg_strain < 8: 
                daily_target -= 200

            # Safety Floor: Never drop below 1500 (unless petite, but safe default)
            if daily_target < 1500: daily_target = 1500

            # 4. BUILD SCHEDULE
            schedule = self._build_daily_schedule(profile, daily_target)
            
            total_week_cals += daily_target

            daily_plans.append(DayPlan(
                day_name=day,
                target_calories=int(daily_target),
                schedule=schedule
            ))
        
        avg_intake = int(total_week_cals / 7)
        
        return WeeklyPlan(
            summary=f"Goal: {goal}. Avg Intake: {avg_intake} kcal vs Burn: {metrics.avg_daily_burn} kcal.",
            daily_plans=daily_plans
        )

    def _build_daily_schedule(self, profile, total_cals) -> list:
        slots = []
        is_workout_day = profile.avg_workout_time != "Rest Day"
        
        try: wake_h = int(profile.avg_wake_time.split(":")[0])
        except: wake_h = 7

        workout_h = 17 
        if is_workout_day:
            try: workout_h = int(profile.avg_workout_time.split(":")[0])
            except: workout_h = 17

        # --- MEAL 1: BREAKFAST ---
        m1_h = wake_h + 1
        if is_workout_day and workout_h <= wake_h + 1: m1_h = workout_h + 1
            
        cat = "breakfast_high_fat"
        if is_workout_day and workout_h < 12: cat = "breakfast_high_carb"
            
        m1_rec = self._get_scaled_recipe(cat, total_cals * 0.35)
        slots.append(MealSlot(self._fmt_time(m1_h), "Meal 1 (Break-Fast)", m1_rec, "Satiety & Focus"))

        # --- MEAL 2: LUNCH ---
        m2_h = m1_h + 4
        m2_rec = self._get_scaled_recipe("lunch_light", total_cals * 0.30)
        slots.append(MealSlot(self._fmt_time(m2_h), "Meal 2 (Lunch)", m2_rec, "Sustained Energy"))

        # --- SNACK (Optional) ---
        if is_workout_day and workout_h > 12:
            snack_h = workout_h - 1
            if snack_h > m2_h + 1:
                snack_rec = self._get_scaled_recipe("snacks", 200)
                slots.append(MealSlot(self._fmt_time(snack_h), "Pre-Workout Fuel", snack_rec, "Quick Glycogen"))

        # --- MEAL 3: DINNER ---
        m3_h = 18
        if is_workout_day and workout_h >= 17: m3_h = workout_h + 1
        if m3_h > 20: m3_h = 20
        if m3_h <= m2_h: m3_h = m2_h + 3

        m3_rec = self._get_scaled_recipe("dinner_recovery", total_cals * 0.35)
        slots.append(MealSlot(self._fmt_time(m3_h), "Meal 3 (Dinner)", m3_rec, "Deep Recovery"))

        return slots

    def _fmt_time(self, hour: int) -> str:
        if hour >= 24: hour -= 24
        suffix = "AM"
        display_h = hour
        if hour >= 12:
            suffix = "PM"
            if hour > 12: display_h -= 12
        elif hour == 0: display_h = 12
        return f"{display_h}:00 {suffix}"

    def _get_scaled_recipe(self, category, target_cals) -> Recipe:
        template = random.choice(RECIPE_VAULT[category])
        
        ratios = {
            "breakfast_high_fat":  [0.30, 0.65, 0.05],
            "breakfast_high_carb": [0.30, 0.10, 0.60], 
            "lunch_light":         [0.40, 0.40, 0.20], 
            "dinner_recovery":     [0.30, 0.20, 0.50], 
            "snacks":              [0.10, 0.00, 0.90]  
        }
        
        split = ratios.get(category, [0.3, 0.35, 0.35])
        
        p = int((target_cals * split[0]) / 4)
        f = int((target_cals * split[1]) / 9) 
        c = int((target_cals * split[2]) / 4) 
        
        base = template.get('base_cals', 500)
        ratio = target_cals / base
        
        return Recipe(
            title=template['title'],
            description=template['desc'],
            ingredients_text=f"Portion scaled {ratio:.1f}x",
            macros=f"~{p}g P | ~{f}g F | ~{c}g C",
            calories=int(target_cals),
            search_query=template['query']
        )
