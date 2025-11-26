import random
from src.models import WeeklyMetrics, WeeklyPlan, DayPlan, MealSlot, Recipe
from src.config import RECIPE_VAULT

class MealPlanner:
    def generate_precision_week(self, metrics: WeeklyMetrics, goal: str) -> WeeklyPlan:
        daily_plans = []
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # 1. DETERMINE GOAL OFFSET
        offset = 0
        if goal == "Lose 1 lb/week": offset = -500
        elif goal == "Gain 1 lb/week": offset = 500
        
        total_week_cals = 0

        for day in days:
            profile = metrics.weekday_profiles.get(day)
            if not profile: continue

            # 2. SET DAILY TARGET (Burn + Goal)
            daily_target = metrics.avg_daily_burn + offset

            # Strain Adjustment (Fuel the work)
            if profile.avg_strain > 14: daily_target += 200 
            elif profile.avg_strain < 8: daily_target -= 200

            # Safety Floor
            if daily_target < 1400: daily_target = 1400

            # 3. BUILD SCHEDULE (Adaptive)
            # We pass the target, but we accept the 'actual' sum returned
            schedule, actual_cals = self._build_daily_schedule(profile, int(daily_target))
            
            total_week_cals += actual_cals

            daily_plans.append(DayPlan(
                day_name=day,
                target_calories=int(daily_target), 
                schedule=schedule 
                # Note: UI compares target vs actual_cals derived from schedule
            ))
        
        avg_intake = int(total_week_cals / 7)
        return WeeklyPlan(
            summary=f"Goal: {goal}. Avg Intake: {avg_intake} kcal vs Burn: {metrics.avg_daily_burn} kcal.",
            daily_plans=daily_plans
        )

    def _build_daily_schedule(self, profile, daily_target) -> tuple[list, int]:
        slots = []
        current_cals = 0
        is_workout_day = profile.avg_workout_time != "Rest Day"
        
        # --- TIME PARSING ---
        try: wake_h = int(profile.avg_wake_time.split(":")[0])
        except: wake_h = 7
        
        workout_h = 17 
        if is_workout_day:
            try: workout_h = int(profile.avg_workout_time.split(":")[0])
            except: workout_h = 17

        # --- STEP 1: PLAN CORE MEALS (Aim for ~85% of daily needs from meals) ---
        # We intentionally under-shoot slightly to leave room for potential snacks
        # or just accept a lighter day.
        
        meal_target = daily_target * 0.28 # Target roughly 28-30% per meal
        
        # 1. BREAKFAST
        m1_h = wake_h + 1
        if is_workout_day and workout_h <= wake_h + 1: m1_h = workout_h + 1
        
        cat = "breakfast_high_fat"
        if is_workout_day and workout_h < 12: cat = "breakfast_high_carb"
        
        rec1 = self._get_scaled_recipe(cat, meal_target)
        slots.append(MealSlot(self._fmt_time(m1_h), "Meal 1 (Break-Fast)", rec1, "Satiety & Focus"))
        current_cals += rec1.calories

        # 2. LUNCH
        m2_h = m1_h + 4
        rec2 = self._get_scaled_recipe("lunch_light", meal_target)
        slots.append(MealSlot(self._fmt_time(m2_h), "Meal 2 (Lunch)", rec2, "Sustained Energy"))
        current_cals += rec2.calories

        # 3. DINNER (Slightly larger budget for recovery)
        m3_h = 18
        if is_workout_day and workout_h >= 17: m3_h = workout_h + 1
        if m3_h > 20: m3_h = 20
        if m3_h <= m2_h: m3_h = m2_h + 3
        
        rec3 = self._get_scaled_recipe("dinner_recovery", meal_target * 1.1) # 10% larger dinner
        slots.append(MealSlot(self._fmt_time(m3_h), "Meal 3 (Dinner)", rec3, "Deep Recovery"))
        current_cals += rec3.calories

        # --- STEP 2: GAP ANALYSIS & SNACKING ---
        # If we are significantly under target, add snacks.
        
        # Gap Threshold: If we are more than 250 cals under, eat.
        gap = daily_target - current_cals
        snack_count = 0
        
        # SNACK 1 Loop
        if gap > 200:
            snack_h = m2_h + 3 # Default: Afternoon snack
            label = "Afternoon Fuel"
            
            # Logic: If workout is in afternoon, move snack to Pre-Workout
            if is_workout_day and workout_h > 12:
                snack_h = workout_h - 1
                label = "Pre-Workout Fuel"
            
            # Find a snack that roughly fits the gap (or at least 1 serving)
            rec_s1 = self._get_scaled_recipe("snacks", gap) 
            # (The scaling function handles rounding, so if gap is huge it might give 2 servings)
            
            slots.append(MealSlot(self._fmt_time(snack_h), label, rec_s1, "Caloric Bridge"))
            current_cals += rec_s1.calories
            gap = daily_target - current_cals
            snack_count += 1

        # SNACK 2 Loop (If still hungry/under-fueled)
        # Only if user is gaining weight or very active
        if gap > 200 and snack_count < 2:
            # Place it mid-morning or post-dinner depending on schedule
            s2_h = m1_h + 2
            if s2_h >= m2_h: s2_h = m3_h + 2 # Late night snack
            
            rec_s2 = self._get_scaled_recipe("snacks", gap)
            slots.append(MealSlot(self._fmt_time(s2_h), "Metabolic Top-Up", rec_s2, "Goal Support"))
            current_cals += rec_s2.calories

        # Sort slots by time so snacks appear in correct order
        slots.sort(key=lambda x: self._parse_time_sort(x.time))

        return slots, current_cals

    def _parse_time_sort(self, time_str):
        # Helper to sort "8:00 AM" vs "1:00 PM" correctly
        parts = time_str.split() # ["8:00", "AM"]
        hm = parts[0].split(":")
        h = int(hm[0])
        is_pm = parts[1] == "PM"
        if is_pm and h != 12: h += 12
        if not is_pm and h == 12: h = 0
        return h

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
        
        base_cals = template.get('base_cals', 500)
        base_p = template.get('p', 20)
        base_f = template.get('f', 20)
        base_c = template.get('c', 20)
        
        # SCALING LOGIC:
        # 1. Ideal Ratio
        raw_ratio = target_cals / base_cals
        
        # 2. Round to nearest WHOLE serving
        # (Unless it rounds to 0, then force 1)
        servings = max(1, round(raw_ratio))
        
        # 3. Recalculate REAL numbers based on the rounded serving
        final_cals = int(base_cals * servings)
        p = int(base_p * servings)
        f = int(base_f * servings)
        c = int(base_c * servings)
        
        return Recipe(
            title=template['title'] + f" ({servings} Srv)",
            description=template['desc'],
            ingredients_text=f"Portion scaled to {servings} servings",
            macros=f"{p}g P | {f}g F | {c}g C",
            calories=final_cals, 
            search_query=template['query']
        )
