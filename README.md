# UrbanPulse AI

### Autonomous Climate Risk Resolution System

## Overview

**UrbanPulse AI** is an intelligent, multi-agent system designed to **detect, evaluate, and respond to climate-induced financial risks affecting urban micro-economies in real time**.

It models how an **autonomous insurance or governance system** can:

- Monitor environmental conditions (e.g., rainfall)
- Assess impact on **street vendors and local markets**
- Quantify financial risk using **Value-at-Risk (VaR)**
- Automatically trigger actions (**Alert / Payout**)
- Generate **explainable audit reports for transparency**

> The system addresses the challenge of delayed and manual disaster response by enabling **fast, data-driven, and explainable decision-making**.

## Problem Statement

Urban ecosystems—especially **street vendors and micro-economies**—are highly vulnerable to sudden climate events like heavy rainfall.

Current systems:

* Lack **real-time response**
* Are **manual and slow**
* Do not provide **explainable decisions**

---

## Our Solution

UrbanPulse AI introduces a **fully autonomous decision pipeline** powered by AI agents:

> From rainfall detection → to financial risk → to automated action.

---

##  System Architecture

###  Multi-Agent Pipeline

1. **Ingestion Agent**

   * Fetches real-time weather data (Open-Meteo integration ready)
   * Supports simulation for testing scenarios

2. **Prediction Agent**

   * Estimates probability of disruption using LLM / fallback logic

3. **Verification Agent**

   * Validates whether the event is significant

4. **Impact Agent**

   * Calculates **Value-at-Risk (VaR)** using:

     * Vendor count
     * Average loss

5. **Decision Agent**

   * Determines action:

     * `NO ACTION`
     * `ALERT`
     * `PAYOUT`

6. **Audit Agent**

   * Generates **Explainable AI decision memo**

---

## Dual-Mode Intelligence

UrbanPulse supports:

| Mode                | Description                                          |
| ------------------- | ---------------------------------------------------- |
| **Simulation Mode** | Controlled rainfall via UI slider (for demo/testing) |
| **Real Mode**       | Ready for live API integration (Open-Meteo)          |

> This allows **deterministic testing of extreme scenarios**, critical in risk systems.

---

## Key Features

 **Real-time AI decision pipeline**
 **LLM-powered reasoning**
 **Value-at-Risk (VaR) calculation**
 **Geospatial visualization (Streamlit map)**
 **Audit logging (persistent logs)**
 **Explainable AI (Decision Memo)**
 **Simulation for stress testing**

---

## Project Structure

```
UrbanPulse AI/
│
├── agents/
│   ├── ingestion_agent.py
│   ├── prediction_agent.py
│   ├── verification_agent.py
│   ├── impact_agent.py
│   ├── decision_agent.py
│   └── audit_agent.py
│
├── core/
│   └── orchestrator.py
│
├── data/
│   └── vendors.json
│
├── utils/
│   ├── llm.py
│   ├── logger.py
│   ├── geo.py
│   ├── api.py
│   ├── config.py
│   └── data_loader.py
│
├── logs/
│   └── audit_log.txt
│
├── ui/
│   └── app.py
│
└── README.md
```

---

##  How It Works

1. User selects **city + rainfall simulation**
2. Pipeline executes:

   * Predict → Verify → Impact → Decision
3. System outputs:

   *  Value at Risk
   *  Risk Level
   *  Action Taken
   *  Decision Memo

---

## ▶ Run Locally

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python -m streamlit run ui/app.py
```

---

##  Example Output

* **VaR:** ₹540,000
* **Action:** PAYOUT
* **Risk Level:** High
* **Audit:** AI-generated decision memo explaining the action

---

##  Why This Stands Out

* Moves beyond dashboards → **automated decision systems**
* Combines:

  * AI reasoning
  * Financial modeling
  * Real-world simulation
* Designed like an **enterprise risk engine**

---

##  Future Enhancements

*  Live API integration (Open-Meteo)
*  Hyper-local geofencing
*  Advanced ML risk models
*  Ward-level vendor mapping
*  Historical risk analytics dashboard

---

##  Use Cases

* Government disaster response systems
* Insurance automation platforms
* Smart city infrastructure
* Climate risk monitoring tools

---

##  Author

Built as part of a hackathon project focused on **AI for real-world impact**.

---

##  Final Thought

> “UrbanPulse AI doesn’t just predict risk — it acts on it.”





