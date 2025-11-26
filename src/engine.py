# src/engine.py
from src.models import WeeklyMetrics, WeeklyPlan

class LogicEngine:
    def compute_weekly_strategy(self, metrics: WeeklyMetrics) -> WeeklyPlan:
        summary = ""
        focus = "Balanced"
        
        # 1. Recovery Analysis
        if metrics.avg_recovery < 45:
            focus = "Systemic Inflammation Reset"
            summary = f"Last week's recovery was critically low ({metrics.avg_recovery}%). "
            summary += "This week prioritizes Omega-3s, Turmeric, and elimination of inflammatory triggers."
        elif metrics.is_overreaching:
            focus = "Adrenal Support"
            summary = f"High Strain ({metrics.avg_strain:.1f}) met with low recovery. "
            summary += "Focus on high-quality complex carbs and sleep hygiene."
        else:
            focus = "Performance Prime"
            summary = "Bio-metrics are stable. Optimized for maintenance and training progression."

        # 2. Alcohol Impact
        if metrics.total_alcohol_days > 2:
            summary += " Liver support protocol activated due to alcohol frequency."
            focus += " + Liver Detox"

        return WeeklyPlan(
            summary=summary,
            focus_area=focus,
            daily_plans=[] # To be filled by Planner
        )