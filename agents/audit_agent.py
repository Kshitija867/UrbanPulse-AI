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