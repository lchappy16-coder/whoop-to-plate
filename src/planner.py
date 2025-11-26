import random
from src.models import WeeklyMetrics, WeeklyPlan, DayPlan, MealSlot, Recipe
from src.config import RECIPE_VAULT

class MealPlanner:
    def generate_precision_week(self, metrics: WeeklyMetrics, goal: str) -> WeeklyPlan:
        daily_plans = []
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # 1. DETERMINE GOAL OFFSET
        offset = 0
        if goal == "Lose 1 lb/week":
            offset = -500
        elif goal == "Gain 1 lb/week":
            offset = 500
        
        total_week_cals = 0

        for day in days:
            profile = metrics.weekday_profiles.get(day)
            if not profile: continue

            # 2. CALORIE MATH
            # Baseline: Daily Burn + Goal Offset
            daily_target = metrics.avg_daily_burn + offset

            # Strain Adjustment
            if profile.avg_strain > 14: 
                daily_target += 200 
            elif profile.avg_strain < 8: 
                daily_target -= 200

            # Safety Floor
            if daily_target < 1400: daily_target = 1400

            # 3. BUILD SCHEDULE (Pass target as Integer)
            schedule = self._build_daily_schedule(profile, int(daily_target))
            
            # Recalculate exact total from schedule to be honest in summary
            exact_total = sum(s.recipe.calories for s in schedule)
            total_week_cals += exact_total

            daily_plans.append(DayPlan(
                day_name=day,
                target_calories=exact_total, # Set target to exactly what we planned
                schedule=schedule
            ))
        
        avg_intake = int(total_week_cals / 7)
        
        return WeeklyPlan(
            summary=f"Goal: {goal}. Avg Intake: {avg_intake} kcal vs Burn: {metrics.avg_daily_burn} kcal.",
            daily_plans=daily_plans
        )

    def _build_daily_schedule(self, profile, total_budget_cals) -> list:
        slots = []
        is_workout_day = profile.avg_workout_time != "Rest Day"
        
        # --- TIME PARSING ---
        try: wake_h = int(profile.avg_wake_time.split(":")[0])
        except: wake_h = 7
        
        workout_h = 17 
        if is_workout_day:
            try: workout_h = int(profile.avg_workout_time.split(":")[0])
            except: workout_h = 17

        # --- CALORIE BUDGETING (The Fix) ---
        remaining_cals = total_budget_cals
        
        # 1. Determine if Snack is needed
        needs_snack = False
        snack_cals = 0
        
        if is_workout_day and workout_h > 12:
            # If working out in afternoon, set aside snack budget
            needs_snack = True
            snack_cals = 250
            remaining_cals -= snack_cals

        # 2. Split Main Meals (35% / 30% / 35% of REMAINDER)
        # We use int() to strip decimals
        m1_cals = int(remaining_cals * 0.35)
        m2_cals = int(remaining_cals * 0.30)
        
        # 3. Assign Remainder to Dinner (Fixes rounding errors)
        # This ensures m1 + m2 + m3 + snack == total_budget_cals EXACTLY
        m3_cals = remaining_cals - m1_cals - m2_cals

        # --- SCHEDULING ---

        # MEAL 1
        m1_h = wake_h + 1
        if is_workout_day and workout_h <= wake_h + 1: m1_h = workout_h + 1
        
        cat = "breakfast_high_fat"
        if is_workout_day and workout_h < 12: cat = "breakfast_high_carb"
        
        m1_rec = self._get_scaled_recipe(cat, m1_cals)
        slots.append(MealSlot(self._fmt_time(m1_h), "Meal 1 (Break-Fast)", m1_rec, "Satiety & Focus"))

        # MEAL 2
        m2_h = m1_h + 4
        m2_rec = self._get_scaled_recipe("lunch_light", m2_cals)
        slots.append(MealSlot(self._fmt_time(m2_h), "Meal 2 (Lunch)", m2_rec, "Sustained Energy"))

        # SNACK (If allocated)
        if needs_snack:
            snack_h = workout_h - 1
            if snack_h > m2_h + 1:
                snack_rec = self._get_scaled_recipe("snacks", snack_cals)
                slots.append(MealSlot(self._fmt_time(snack_h), "Pre-Workout Fuel", snack_rec, "Quick Glycogen"))

        # MEAL 3
        m3_h = 18
        if is_workout_day and workout_h >= 17: m3_h = workout_h + 1
        if m3_h > 20: m3_h = 20
        if m3_h <= m2_h: m3_h = m2_h + 3

        m3_rec = self._get_scaled_recipe("dinner_recovery", m3_cals)
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
            calories=int(target_cals), # Pass the integer target directly
            search_query=template['query']
        )
