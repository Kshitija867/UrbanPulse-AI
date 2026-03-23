from agents.ingestion_agent import ingestion_agent
from agents.prediction_agent import prediction_agent
from agents.verification_agent import verification_agent
from agents.impact_agent import impact_agent
from agents.decision_agent import decision_agent
from agents.audit_agent import audit_agent

def run_pipeline(location):
    context = ingestion_agent(location)
    prediction = prediction_agent(context)
    verification = verification_agent(context, prediction)

    if not verification["verified"]:
        return {"status": "No Action Needed"}

    impact = impact_agent(context)
    decision = decision_agent(impact)
    audit = audit_agent(context, prediction, verification, impact, decision)

    return {
        "context": context,
        "prediction": prediction,
        "impact": impact,
        "decision": decision,
        "audit": audit
    }