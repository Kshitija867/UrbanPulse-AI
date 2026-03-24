from utils.llm import ask_llm

def audit_agent(context, prediction, verification, impact, decision):
    prompt = f"""
    Create a professional decision memo:

    Rainfall: {context['simulated_rain']}
    Probability: {prediction['rain_probability']}%
    Verified: {verification['verified']}
    Vendors: {impact['vendors']}
    VaR: ₹{impact['VaR']}
    Action: {decision['action']}

    Explain WHY this action was taken.
    """

    memo = ask_llm(prompt)

    return {"log": memo}

# def audit_agent(context, prediction, verification, impact, decision):

#     rain = context.get("precipitation", 0)
#     prob = prediction.get("rain_probability", 0)
#     verified = verification.get("verified", False)

#     vendors = impact.get("vendors", 0)
#     var = impact.get("VaR", 0)
#     action = decision.get("action", "NONE")

#     log = f"""
# Decision Memo

# Rainfall: {rain} mm/hr
# Probability: {prob}%
# Verified: {verified}

# Vendors Affected: {vendors}
# Value at Risk: ₹{var}

# Final Action: {action}
# """

#     return {"log": log}