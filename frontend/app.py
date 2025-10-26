import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import time
from backend.solver import find_max_weeks
# --- Streamlit setup ---
st.set_page_config(page_title="Social Golfers Problem Solver", page_icon="⛳", layout="wide")
st.title("🏌️ Social Golfers Problem")

st.caption("Given the number of players and group size, the solver finds the **maximum number of weeks** players can play without any two appearing together twice.")

# --- INPUTS ---
num_players = st.number_input("Number of players (n)", min_value=4, max_value=64, value=32, step=4, key="num_players")
group_size = st.number_input("Players per group (p)", min_value=2, max_value=8, value=4, key="group_size")
algorithm = st.selectbox("Select algorithm", ["Depth-First Search (DFS)", "Depth-Limited Search (DLS)"], key="algo")
depth_limit = st.number_input("Depth limit (for DLS)", min_value=1, max_value=20, value=5, key="depth_limit")
max_attempt = st.number_input("Maximum weeks to test", min_value=1, max_value=15, value=8, key="max_weeks")

if num_players % group_size != 0:
    st.error("❌ The number of players must be divisible by the group size!")
    st.stop()

num_groups = num_players // group_size
st.info(f"➡️ Each week will have {num_groups} groups of {group_size} players.")

st.divider()

# --- Progress UI ---
progress_bar = st.progress(0)
status_text = st.empty()

def update_progress(current, total, message):
    progress = int((current / total) * 100)
    progress_bar.progress(progress)
    status_text.info(message)

# --- Solve Button ---
if st.button("🧠 Find Maximum Weeks", key="solve_button"):
    start = time.time()
    with st.spinner("Optimizing schedule..."):
        result, max_found = find_max_weeks(
            num_players,
            group_size,
            algorithm,
            depth_limit,
            max_attempt=max_attempt,
            progress_callback=update_progress
        )
    elapsed = time.time() - start

    progress_bar.progress(100)
    status_text.info("✅ Search complete!")

    if result:
        st.success(f"✅ Maximum feasible weeks: **{max_found}** (found in {elapsed:.2f}s)")
        for i, week in enumerate(result, 1):
            st.markdown(f"### Week {i}")
            for j, group in enumerate(week, 1):
                st.write(f"Group {j}: {group}")
    else:
        st.error(f"❌ No valid schedule found (elapsed: {elapsed:.2f}s). Try fewer players or smaller groups.")
