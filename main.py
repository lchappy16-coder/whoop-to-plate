# main.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.ingestion import IngestionEngine
from src.planner import MealPlanner

def print_week(plan):
    print(f"\n{'='*80}")
    print(f"   🥗 WHOOP PRECISION NUTRITION PLAN")
    print(f"   {plan.summary}")
    print(f"{'='*80}")

    for day in plan.daily_plans:
        actual_total = sum(slot.recipe.calories for slot in day.schedule)
        
        print(f"\n📅 {day.day_name.upper()}") 
        print(f"   🎯 Daily Target: {day.target_calories} kcal")
        print(f"   📊 Actual Sum:   {actual_total} kcal")
        print(f"   {'-'*60}")
        
        for slot in day.schedule:
            print(f"   ⏰ {slot.time} | {slot.type}")
            print(f"      🍲 {slot.recipe.title} -- [{slot.recipe.calories} kcal]")
            print(f"         \"{slot.recipe.description}\"")
            # UPDATED LABELS HERE
            print(f"         Macros: {slot.recipe.macros}")
            print(f"         Google: \"{slot.recipe.search_query}\"")
            print("")
        print(f"{'='*80}")

if __name__ == "__main__":
    try:
        ingestor = IngestionEngine()
        ingestor.load_data_interactive()
        
        metrics = ingestor.analyze_patterns()
        
        chef = MealPlanner()
        plan = chef.generate_precision_week(metrics)
        
        print_week(plan)
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter...")