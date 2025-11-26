# src/models.py
from dataclasses import dataclass, field
from typing import List, Dict
import datetime

@dataclass
class WeekdayProfile:
    day_name: str         # "Monday"
    avg_wake_time: str    # "07:30"
    avg_workout_time: str # "17:00"
    avg_strain: float     # 14.5

@dataclass
class WeeklyMetrics:
    start_date: datetime.date
    end_date: datetime.date
    weekday_profiles: Dict[str, WeekdayProfile] # Map "Monday" -> Profile
    avg_daily_burn: int
    avg_recovery: int
    focus_area: str

@dataclass
class Recipe:
    title: str
    description: str
    ingredients_text: str # "6oz Steak, 1 cup Rice..."
    macros: str           # "P: 40g | C: 50g | F: 20g"
    calories: int
    search_query: str     # String to help user find similar recipes online

@dataclass
class MealSlot:
    time: str
    type: str             # "Break-Fast", "Pre-Workout", "Recovery Dinner"
    recipe: Recipe
    reasoning: str

@dataclass
class DayPlan:
    day_name: str
    target_calories: int
    schedule: List[MealSlot]

@dataclass
class WeeklyPlan:
    summary: str
    daily_plans: List[DayPlan] = field(default_factory=list)