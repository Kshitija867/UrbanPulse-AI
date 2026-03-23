def prediction_agent(context):
    rain = context["precipitation"]

    probability = min(100, rain * 10)

    return {
        "rain_probability": probability
    }