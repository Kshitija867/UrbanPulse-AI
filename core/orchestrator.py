from agents.prediction_agent import prediction_agent
from agents.verification_agent import verification_agent
from agents.impact_agent import impact_agent
from agents.decision_agent import decision_agent
from agents.audit_agent import audit_agent
from utils.data_loader import load_vendors
from utils.logger import log_decision

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
        "avg_loss": selected["avg_loss"],
        "vendor_coords": (selected["lat"], selected["lon"])
    }

    prediction = prediction_agent(context)
    verification = verification_agent(context)

    if not verification["verified"]:
        return {"status": "No Action Needed"}

    impact = impact_agent(context)
    decision = decision_agent(impact)
    audit = audit_agent(context, prediction, verification, impact, decision)

    # RESULT OBJECT
    result = {
        "prediction": prediction,
        "impact": impact,
        "decision": decision,
        "audit": audit
    }

    
    log_decision(result)

    return result