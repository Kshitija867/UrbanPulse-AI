# smarter explanation
from utils.llm import ask_llm

# def impact_agent(context):
#     vendors = 450
#     avg_loss = 800
#     multiplier = context["multiplier"]

#     var = vendors * avg_loss * multiplier

#     prompt = f"""
#     Explain in 1 sentence:
#     Why is a financial risk of ₹{var} significant for a local market ecosystem?
#     """

#     explanation = ask_llm(prompt)

#     return {
#         "vendors": vendors,
#         "avg_loss": avg_loss,
#         "VaR": var,
#         "explanation": explanation
#     }

def impact_agent(context):
    rain = context.get("simulated_rain", 0)

    # simple multiplier logic
    if rain > 15:
        multiplier = 1.5
    elif rain > 10:
        multiplier = 1.2
    else:
        multiplier = 0.8

    # default values (since we removed vendor DB for now)
    vendors = context.get("vendors", 400)
    avg_loss = context.get("avg_loss", 800)

    var = int(vendors * avg_loss * multiplier)

    return {
        "VaR": var,
        "vendors": vendors,
        "avg_loss": avg_loss,
        "explanation": f"Estimated loss of ₹{var} due to rainfall impact."
    }