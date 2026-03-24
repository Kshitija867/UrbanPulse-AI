import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import time
import pandas as pd 
from core.orchestrator import run_pipeline

st.set_page_config(page_title="UrbanPulse AI", layout="wide")

st.title("UrbanPulse AI Command Center")

location = st.selectbox("Select Location", ["Pune", "Mumbai", "Delhi"])

# ---- COMBINED MAP (VENDORS + SELECTED LOCATION) ----
coords = {
    "Pune": (18.52, 73.85),
    "Mumbai": (19.07, 72.87),
    "Delhi": (28.61, 77.20)
}

vendor_data = pd.DataFrame([
    {"lat": 18.516, "lon": 73.856},   # Pune - Laxmi Road
    {"lat": 18.5204, "lon": 73.8410}, # Pune - FC Road
    {"lat": 18.5679, "lon": 73.9143}, # Pune - Viman Nagar

    {"lat": 19.0176, "lon": 72.8562}, # Mumbai - Dadar
    {"lat": 19.1136, "lon": 72.8697}, # Mumbai - Andheri

    {"lat": 28.6519, "lon": 77.1909}, # Delhi - Karol Bagh
    {"lat": 28.6562, "lon": 77.2300}  # Delhi - Chandni Chowk
])

# Selected location point
selected_point = pd.DataFrame({
    "lat": [coords[location][0]],
    "lon": [coords[location][1]]
})

# Merge both
map_data = pd.concat([vendor_data, selected_point], ignore_index=True)

st.subheader("Geospatial View")
st.map(map_data)


# ---- SESSION STATE ----
if "result" not in st.session_state:
    st.session_state.result = None

def format_currency(value):
    return f"₹{value:,.0f}"

# ---- RAIN SLIDER ----
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

        # ---- RUN PIPELINE ----
        st.session_state.result = run_pipeline(
            coords[location],
            simulated_rain=rain_input
        )

        st.write("Audit Agent: Generating decision memo...")
        time.sleep(1)

    status.update(label="Analysis Complete!", state="complete")


# ---- DISPLAY RESULT ----
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

        # ---- ADDED: MARKET CONTEXT ----
        st.subheader("Selected Market Context")
        st.write(f"Vendors: {result['impact']['vendors']}")
        st.write(f"Avg Loss per Vendor: ₹{result['impact']['avg_loss']}")

        st.divider()

        # AI Insight
        st.subheader("AI Insight")
        st.info(result["impact"]["explanation"])

        st.divider()

        # Decision Memo
        st.subheader("Decision Memo (Explainable AI)")
        st.code(result["audit"]["log"], language="markdown")

    else:
        st.warning("No significant risk detected")