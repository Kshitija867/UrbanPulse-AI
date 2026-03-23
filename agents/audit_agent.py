def audit_agent(context, prediction, verification, impact, decision):
    return {
        "log": f"""
Rain: {context['precipitation']}
Probability: {prediction['rain_probability']}%
Verified: {verification['verified']}
VaR: ₹{impact['VaR']}
Action: {decision['action']}
"""
    }