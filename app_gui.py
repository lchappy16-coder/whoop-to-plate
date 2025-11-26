import streamlit as st
import pandas as pd
import sys
import os

# --- PATH CONFIGURATION ---
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from src.ingestion import IngestionEngine
from src.planner import MealPlanner

# --- 1. PAGE CONFIG & STYLING ---
st.set_page_config(
    page_title="WHOOP© to Plate",
    page_icon="🧬",
    layout="wide"
)

# MODERN HIGH-CONTRAST CSS
st.markdown("""
<style>
    /* 1. FORCE TEXT COLOR */
    .stApp, .stMarkdown, h1, h2, h3, h4, h5, h6, p, li, span, div {
        color: #E0E0E0 !important;
    }
    
    /* 2. BACKGROUND */
    .stApp {
        background-color: #0E1117;
    }

    /* 3. UPLOAD CARDS */
    .upload-card {
        background-color: #161B22;
        border: 1px dashed #30363D;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    }
    
    /* 4. MEAL CARDS */
    .meal-card {
        background-color: #1E1E1E;
        border: 1px solid #333;
        border-left: 4px solid #00C805;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    
    /* 5. METRICS */
    div[data-testid="stMetricValue"] {
        color: #00C805 !important;
        font-size: 28px !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #8B949E !important;
    }

    /* 6. BUTTONS */
    div.stButton > button {
        background-color: #00C805;
        color: white !important;
        border: none;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 8px;
        transition: all 0.2s;
    }
    div.stButton > button:hover {
        background-color: #00E006;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
c1, c2 = st.columns([1, 5])
with c1:
    st.write("🧬 **WHOOP© TO PLATE**")
with c2:
    pass 

st.divider()

# --- 3. INPUT SECTION ---
if 'plan_generated' not in st.session_state:
    st.session_state.plan_generated = False

# HEADER TEXT
st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>Initialize Protocol</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8B949E !important; margin-bottom: 40px;'>Upload your raw WHOOP© exports to generate a precision nutrition strategy.</p>", unsafe_allow_html=True)

# THE 2x2 GRID
col1, col2 = st.columns(2, gap="large")

with col1:
    f1 = st.file_uploader("Cycles (physiological_cycles.csv)", type="csv")
    f2 = st.file_uploader("Workouts (workouts.csv)", type="csv")

with col2:
    f3 = st.file_uploader("Sleeps (sleeps.csv)", type="csv")
    f4 = st.file_uploader("Journal (journal_entries.csv)", type="csv")

# ACTION BUTTON
st.markdown("<br>", unsafe_allow_html=True)
center_col1, center_col2, center_col3 = st.columns([1, 2, 1])

with center_col2:
    if f1 and f2 and f3 and f4:
        if st.button("🚀 RUN ANALYSIS ENGINE", use_container_width=True):
            with st.spinner("Triangulating Circadian Rhythm & Metabolic Load..."):
                try:
                    ingestor = IngestionEngine()
                    files_map = {
                        "physiological_cycles.csv": f1,
                        "workouts.csv": f2,
                        "sleeps.csv": f3,
                        "journal_entries.csv": f4
                    }
                    ingestor.load_from_memory(files_map)
                    metrics = ingestor.analyze_patterns()
                    
                    chef = MealPlanner()
                    plan = chef.generate_precision_week(metrics)
                    
                    st.session_state.metrics = metrics
                    st.session_state.plan = plan
                    st.session_state.plan_generated = True
                    st.rerun() 
                    
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.info("Waiting for all 4 files...", icon="⏳")

# --- 4. DASHBOARD ---
if st.session_state.plan_generated:
    st.divider()
    plan = st.session_state.plan
    metrics = st.session_state.metrics
    
    st.success(f"**PROTOCOL GENERATED:** {plan.summary}")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Daily Burn", f"{metrics.avg_daily_burn}", "kcal")
    m2.metric("Recovery Avg", f"{metrics.avg_recovery}%", "WHOOP©")
    strain_avg = sum(p.avg_strain for p in metrics.weekday_profiles.values())/7
    m3.metric("Weekly Strain", f"{strain_avg:.1f}", "Load")
    m4.metric("Strategy", metrics.focus_area)
    
    st.markdown("<br>", unsafe_allow_html=True)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    tabs = st.tabs([f"  {d}  " for d in days])

    for i, day_name in enumerate(days):
        with tabs[i]:
            day_plan = next((d for d in plan.daily_plans if d.day_name == day_name), None)
            
            if day_plan:
                c_a, c_b = st.columns([3, 1])
                with c_a:
                    st.markdown(f"### 📅 {day_name} Schedule")
                with c_b:
                    st.markdown(f"<div style='text-align:right; font-size:1.5em; color:#00C805; font-weight:bold;'>{day_plan.target_calories} kcal</div>", unsafe_allow_html=True)
                
                st.markdown("---")
                
                for slot in day_plan.schedule:
                    st.markdown(f"""
                    <div class="meal-card">
                        <div style="display:flex; justify-content:space-between; color:#8B949E; margin-bottom:5px;">
                            <span>⏰ <b>{slot.time}</b></span>
                            <span>{slot.type}</span>
                        </div>
                        <h3 style="color:#FFF !important; margin:0;">{slot.recipe.title}</h3>
                        <p style="color:#CCC !important; font-style:italic;">{slot.recipe.description}</p>
                        <div style="background:#111; padding:10px; border-radius:5px; display:flex; justify-content:space-between;">
                            <span style="font-family:monospace; color:#DDD;">{slot.recipe.macros}</span>
                            <span style="color:#00C805; font-weight:bold;">{slot.recipe.calories} kcal</span>
                        </div>
                        <div style="margin-top:10px;">
                            <a href="https://www.google.com/search?q={slot.recipe.search_query.replace(' ', '+')}" target="_blank" style="color:#00C805; text-decoration:none; font-weight:bold;">🔎 Search Recipe &rarr;</a>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    if st.button("⬅️ Start Over"):
        st.session_state.plan_generated = False
        st.rerun()
