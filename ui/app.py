import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from core.orchestrator import run_pipeline

st.title("UrbanPulse AI Command Center")

location = st.selectbox("Select Location", ["Pune", "Mumbai", "Delhi"])

coords = {
    "Pune": (18.52, 73.85),
    "Mumbai": (19.07, 72.87),
    "Delhi": (28.61, 77.20)
}

if st.button("Run Analysis"):
    result = run_pipeline(coords[location])

    st.subheader("Results")

    if "impact" in result:
        st.write("💰 Value at Risk:", result["impact"]["VaR"])
        st.write("⚡ Action:", result["decision"]["action"])
    else:
        st.write("No risk detected")

    st.subheader("Audit Log")
    st.text(result.get("audit", {}).get("log", "No logs"))