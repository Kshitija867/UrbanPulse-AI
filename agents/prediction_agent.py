from utils.llm import ask_llm

def prediction_agent(context):
    rain = context.get("simulated_rain", 0)

    prompt = f"""
    Current rainfall is {rain} mm/hr.

    Predict the probability (0-100%) of severe disruption in next 2 hours.
    Only return a number.
    """

    try:
        result = ask_llm(prompt)
        probability = int(result.strip())
    except:
        probability = min(100, rain * 10)

    return {"rain_probability": probability}
