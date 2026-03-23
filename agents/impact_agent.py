# smarter explanation
from utils.llm import ask_llm

def impact_agent(context):
    vendors = 450
    avg_loss = 800
    multiplier = context["multiplier"]

    var = vendors * avg_loss * multiplier

    prompt = f"""
    Explain in 1 sentence:
    Why is a financial risk of ₹{var} significant for a local market ecosystem?
    """

    explanation = ask_llm(prompt)

    return {
        "vendors": vendors,
        "avg_loss": avg_loss,
        "VaR": var,
        "explanation": explanation
    }