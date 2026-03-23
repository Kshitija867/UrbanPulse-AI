import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import time
from core.orchestrator import run_pipeline

st.set_page_config(page_title="UrbanPulse AI", layout="wide")

st.title("UrbanPulse AI Command Center")

location = st.selectbox("Select Location", ["Pune", "Mumbai", "Delhi"])

coords = {
    "Pune": (18.52, 73.85),
    "Mumbai": (19.07, 72.87),
    "Delhi": (28.61, 77.20)
}

# ---- ADD SESSION STATE ----
if "result" not in st.session_state:
    st.session_state.result = None

def format_currency(value):
    return f"₹{value:,.0f}"

# ---- MOVE SLIDER OUTSIDE BUTTON ----
rain_input = st.slider("Simulate Rainfall (mm/hr)", 0, 20, 5)

if st.button("Run AI Analysis"):

    status = st.status("Initializing AI Agents...", expanded=True)

    with status:
        st.write("Ingestion Agent: Fetching weather data...")
        time.sleep(1)

        st.write("Prediction Agent: Estimating disruption probability...")
        time.sleep(1)

        st.write("Verification Agent: Validating event...")
        time.sleep(1)

        st.write("Impact Agent: Calculating financial risk...")
        time.sleep(1)

        st.write("Decision Agent: Taking action...")
        time.sleep(1)

        # ---- STORE RESULT IN SESSION ----
        st.session_state.result = run_pipeline(
            coords[location],
            simulated_rain=rain_input
        )

        st.write("Audit Agent: Generating decision memo...")
        time.sleep(1)

    status.update(label="Analysis Complete!", state="complete")


# ---- DISPLAY RESULT OUTSIDE BUTTON ----
if st.session_state.result:

    result = st.session_state.result

    if "impact" in result:

        var = result["impact"]["VaR"]
        action = result["decision"]["action"]

        # Risk Color Logic
        if var > 500000:
            risk_color = "High Risk"
        elif var > 200000:
            risk_color = "Medium Risk"
        else:
            risk_color = "Low Risk"

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Value at Risk", format_currency(var))

        with col2:
            st.metric("Action Taken", action)

        with col3:
            st.metric("Risk Level", risk_color)

        st.divider()

        # AI Insight Section
        st.subheader("AI Insight")
        st.info(result["impact"]["explanation"])

        st.divider()

        # Decision Memo
        st.subheader("Decision Memo (Explainable AI)")
        st.code(result["audit"]["log"], language="markdown")

    else:
        st.warning("No significant risk detected")