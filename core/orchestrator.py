# # from agents.ingestion_agent import ingestion_agent
# from agents.prediction_agent import prediction_agent
# from agents.verification_agent import verification_agent
# from agents.impact_agent import impact_agent
# from agents.decision_agent import decision_agent
# from agents.audit_agent import audit_agent
# from utils.data_loader import load_vendors
# from utils.logger import log_decision


# def run_pipeline(coords, location, simulated_rain=0):

#     # Load vendors
#     vendors = load_vendors()

#     # Select vendor based on city
#     selected_vendor = next(
#         (v for v in vendors if v["city"] == location),
#         vendors[0]
#     )

#     # Context (FIXED)
#     context = {
#         "coords": coords,
#         "vendor_location": (selected_vendor["lat"], selected_vendor["lon"]),
#         "vendors": selected_vendor["vendors"],
#         "avg_loss": selected_vendor["avg_loss"],
#         "simulated_rain": simulated_rain,
#         "multiplier": 1
#     }

#     prediction = prediction_agent(context)
#     verification = verification_agent(context)

#     if not verification["verified"]:
#         return {"status": "No Action Needed"}

#     impact = impact_agent(context)
#     decision = decision_agent(impact)
#     audit = audit_agent(context, prediction, verification, impact, decision)

#     result = {
#         "context": context,
#         "prediction": prediction,
#         "impact": impact,
#         "decision": decision,
#         "audit": audit
#     }

#     log_decision(result)

#     return result
from agents.prediction_agent import prediction_agent
from agents.verification_agent import verification_agent
from agents.impact_agent import impact_agent
from agents.decision_agent import decision_agent
from agents.audit_agent import audit_agent
from utils.data_loader import load_vendors

def run_pipeline(coords, simulated_rain=None):

    vendors_data = load_vendors()

    # match by coords (simple safe way)
    if coords == (18.52, 73.85):
        city = "Pune"
    elif coords == (19.07, 72.87):
        city = "Mumbai"
    else:
        city = "Delhi"

    selected = next(
        (v for v in vendors_data if v["city"] == city),
        vendors_data[0]
    )

    context = {
        "coords": coords,
        "simulated_rain": simulated_rain,
        "vendors": selected["vendors"],
        "avg_loss": selected["avg_loss"]
    }

    prediction = prediction_agent(context)
    verification = verification_agent(context)

    if not verification["verified"]:
        return {"status": "No Action Needed"}

    impact = impact_agent(context)
    decision = decision_agent(impact)
    audit = audit_agent(context, prediction, verification, impact, decision)

    return {
        "prediction": prediction,
        "impact": impact,
        "decision": decision,
        "audit": audit
    }