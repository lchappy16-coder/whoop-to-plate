# src/planner.py
import random
from src.models import WeeklyMetrics, WeeklyPlan, DayPlan, MealSlot, Recipe
from src.config import RECIPE_VAULT

class MealPlanner:
    def generate_precision_week(self, metrics: WeeklyMetrics) -> WeeklyPlan:
        daily_plans = []
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for day in days:
            profile = metrics.weekday_profiles.get(day)
            if not profile: continue

            # 1. Calorie Math
            daily_target = metrics.avg_daily_burn
            if profile.avg_strain > 14: daily_target += 300
            elif profile.avg_strain < 8: daily_target -= 200

            # 2. Schedule Logic
            schedule = self._build_daily_schedule(profile, daily_target)
            
            daily_plans.append(DayPlan(
                day_name=day,
                target_calories=int(daily_target),
                schedule=schedule
            ))

        return WeeklyPlan(
            summary=f"Weekly plan calibrated for {metrics.avg_daily_burn} avg burn.",
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
            
        # Default to High Fat (Low Insulin)
        cat = "breakfast_high_fat"
        # If High Strain/Morning Workout -> High Carb
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
        return f"{hour:02d}:00"

    def _get_scaled_recipe(self, category, target_cals) -> Recipe:
        template = random.choice(RECIPE_VAULT[category])
        
        # --- DYNAMIC MACRO SPLITS [Protein, Fat, Carb] ---
        # This fixes the "93g Carb Keto Omelet" bug
        ratios = {
            "breakfast_high_fat":  [0.30, 0.65, 0.05], # 65% Fat, 5% Carb
            "breakfast_high_carb": [0.30, 0.10, 0.60], # 60% Carb
            "lunch_light":         [0.40, 0.40, 0.20], # Moderate
            "dinner_recovery":     [0.30, 0.20, 0.50], # High Carb for sleep
            "snacks":              [0.10, 0.00, 0.90]  # Pure Energy
        }
        
        # Default to balanced if category not found
        split = ratios.get(category, [0.3, 0.35, 0.35])
        
        # Math: (Calories * Percent) / Calories_Per_Gram
        p = int((target_cals * split[0]) / 4) # 4 cal/g
        f = int((target_cals * split[1]) / 9) # 9 cal/g
        c = int((target_cals * split[2]) / 4) # 4 cal/g
        
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