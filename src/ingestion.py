# src/ingestion.py
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import sys
from datetime import timedelta
from src.models import WeeklyMetrics, WeekdayProfile

class IngestionEngine:
    def __init__(self):
        self.files = ["physiological_cycles.csv", "workouts.csv", "sleeps.csv", "journal_entries.csv"]
        self.dfs = {}

    # --- METHOD 1: FOR TERMINAL (Old way) ---
    def load_data_interactive(self):
        root = tk.Tk(); root.withdraw()
        print("\n--- 📂 DATA INGESTION ---")
        for f in self.files:
            print(f"Select [{f}]...")
            path = filedialog.askopenfilename(title=f"Select {f}")
            if not path: sys.exit()
            self.dfs[f] = pd.read_csv(path)
        self._normalize_dates()

    # --- METHOD 2: FOR WEB APP (New way) ---
    def load_from_memory(self, uploaded_files):
        """
        Accepts a dictionary of Streamlit file buffers:
        {'physiological_cycles.csv': file_buffer, ...}
        """
        for filename, buffer in uploaded_files.items():
            if buffer is not None:
                # Seek start to ensure we read from beginning
                buffer.seek(0)
                self.dfs[filename] = pd.read_csv(buffer)
        
        # Verify we have all 4
        if len(self.dfs) < 4:
            raise ValueError(f"Missing files! Only loaded: {list(self.dfs.keys())}")
            
        self._normalize_dates()

    def _normalize_dates(self):
        map_ = {
            "physiological_cycles.csv": "Cycle start time", 
            "workouts.csv": "Cycle start time", 
            "sleeps.csv": "Cycle start time", 
            "journal_entries.csv": "Date"
        }
        for f, df in self.dfs.items():
            col = map_.get(f)
            if f == "journal_entries.csv" and col not in df.columns: col = "Cycle start time"
            
            if col in df.columns:
                df['datetime_obj'] = pd.to_datetime(df[col])
                df['date_obj'] = df['datetime_obj'].dt.date
                df['day_name'] = df['datetime_obj'].dt.day_name()

    def analyze_patterns(self) -> WeeklyMetrics:
        cycles = self.dfs["physiological_cycles.csv"]
        workouts = self.dfs["workouts.csv"]
        sleeps = self.dfs["sleeps.csv"]
        
        # Baseline Averages
        avg_burn = int(cycles['Energy burned (cal)'].mean()) if not cycles.empty else 2000
        avg_rec = int(cycles['Recovery score %'].mean()) if not cycles.empty else 50
        
        profiles = {}
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        for day in days:
            # Wake Logic
            day_sleeps = sleeps[sleeps['day_name'] == day]
            wake_time = "07:00"
            if not day_sleeps.empty:
                wake_hours = []
                for _, row in day_sleeps.iterrows():
                    start = row['datetime_obj']
                    duration = row.get('Time in bed (min)', 480) 
                    wake_dt = start + timedelta(minutes=duration)
                    wake_hours.append(wake_dt.hour + (wake_dt.minute / 60))
                
                if wake_hours:
                    avg_w_h = sum(wake_hours) / len(wake_hours)
                    if 4 <= avg_w_h <= 11:
                        wake_time = f"{int(avg_w_h):02d}:{int((avg_w_h % 1)*60):02d}"

            # Workout Logic
            day_workouts = workouts[workouts['day_name'] == day]
            workout_time = "Rest Day"
            if not day_workouts.empty:
                avg_work_h = day_workouts['datetime_obj'].dt.hour.mean()
                workout_time = f"{int(avg_work_h):02d}:00"
            
            # Strain
            day_cycles = cycles[cycles['day_name'] == day]
            avg_strain = day_cycles['Day Strain'].mean() if not day_cycles.empty else 10.0

            profiles[day] = WeekdayProfile(day, wake_time, workout_time, avg_strain)

        return WeeklyMetrics(
            start_date=cycles['date_obj'].min() if not cycles.empty else None,
            end_date=cycles['date_obj'].max() if not cycles.empty else None,
            weekday_profiles=profiles,
            avg_daily_burn=avg_burn,
            avg_recovery=avg_rec,
            focus_area="Balanced"
        )