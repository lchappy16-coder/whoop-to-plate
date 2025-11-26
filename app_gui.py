# app_gui.py
import streamlit as st
import pandas as pd
import sys
import os

# Connect to the Brain
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.ingestion import IngestionEngine
from src.planner import MealPlanner

# --- 1. PAGE CONFIG & STYLING ---
st.set_page_config(
    page_title="Whoop-to-Plate Pro",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for "Tesla-like" Aesthetics
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Card Styling */
    .meal-card {
        background-color: #1e1e1e;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        transition: transform 0.2s;
    }
    .meal-card:hover {
        border-color: #00c805; /* Whoop Green */
    }
    
    /* Typography */
    h1, h2, h3 { font-family: 'Helvetica Neue', sans-serif; }
    .time-badge {
        background-color: #333;
        color: #fff;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.85em;
        font-weight: bold;
    }
    .macro-text {
        color: #aaa;
        font-size: 0.9em;
        font-family: monospace;
    }
    
    /* Metrics */
    div[data-testid="stMetricValue"] {
        font-size: 24px;
        color: #00c805;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR (INPUTS) ---
with st.sidebar:
    st.title("Data Injection")
    st.caption("Upload your raw CSV exports.")
    
    f1 = st.file_uploader("physiological_cycles.csv", type="csv")
    f2 = st.file_uploader("workouts.csv", type="csv")
    f3 = st.file_uploader("sleeps.csv", type="csv")
    f4 = st.file_uploader("journal_entries.csv", type="csv")
    
    run_btn = st.button("Generate Protocol", type="primary", use_container_width=True)

# --- 3. MAIN APP LOGIC ---
if run_btn and f1 and f2 and f3 and f4:
    try:
        # 1. Ingest Data from Memory
        ingestor = IngestionEngine()
        files_map = {
            "physiological_cycles.csv": f1,
            "workouts.csv": f2,
            "sleeps.csv": f3,
            "journal_entries.csv": f4
        }
        ingestor.load_from_memory(files_map)
        metrics = ingestor.analyze_patterns()
        
        # 2. Plan Meals
        chef = MealPlanner()
        plan = chef.generate_precision_week(metrics)
        
        # 3. Render Dashboard
        st.title("🧬 Precision Nutrition Protocol")
        st.markdown(f"**Focus:** {plan.summary}")
        
        # Top Level Stats
        c1, c2, c3 = st.columns(3)
        c1.metric("Weekly Avg Burn", f"{metrics.avg_daily_burn} kcal")
        c2.metric("Avg Recovery", f"{metrics.avg_recovery}%")
        c3.metric("Avg Strain", f"{sum(p.avg_strain for p in metrics.weekday_profiles.values())/7:.1f}")
        
        st.divider()
        
        # 4. WEEKLY TABS
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        tabs = st.tabs(days)
        
        for i, day_name in enumerate(days):
            with tabs[i]:
                # Find the plan for this day
                day_plan = next((d for d in plan.daily_plans if d.day_name == day_name), None)
                
                if day_plan:
                    actual_cal = sum(s.recipe.calories for s in day_plan.schedule)
                    
                    # Daily Header
                    st.markdown(f"### 📅 {day_name} Protocol")
                    c_a, c_b = st.columns(2)
                    c_a.info(f"**Target:** {day_plan.target_calories} kcal")
                    c_b.success(f"**Actual:** {actual_cal} kcal")
                    
                    # Timeline
                    for slot in day_plan.schedule:
                        # Render Recipe Card
                        with st.container():
                            st.markdown(f"""
                            <div class="meal-card">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                    <span class="time-badge">⏰ {slot.time}</span>
                                    <span style="color:#888; font-size:0.9em;">{slot.type}</span>
                                </div>
                                <h3 style="margin:0 0 5px 0; color:#fff;">{slot.recipe.title}</h3>
                                <p style="color:#ccc; margin-bottom:10px;">{slot.recipe.description}</p>
                                <div style="background:#111; padding:8px; border-radius:6px; margin-bottom:10px;">
                                    <span class="macro-text">{slot.recipe.macros}</span>
                                    <span style="float:right; color:#00c805; font-weight:bold;">{slot.recipe.calories} kcal</span>
                                </div>
                                <a href="https://www.google.com/search?q={slot.recipe.search_query.replace(' ', '+')}" target="_blank" 
                                   style="color:#00c805; text-decoration:none; font-weight:bold; font-size:0.9em;">
                                   🔎 Find Recipe on Google &rarr;
                                </a>
                            </div>
                            """, unsafe_allow_html=True)
                            
    except Exception as e:
        st.error(f"Analysis Failed: {e}")
        import traceback
        st.code(traceback.format_exc())

else:
    # IDLE STATE
    st.markdown("### 👋 Welcome to Whoop-to-Plate")
    st.info("Please drag and drop your 4 Whoop CSV files into the sidebar to begin.")