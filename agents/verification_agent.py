def verification_agent(context, prediction):
    if prediction["rain_probability"] > 50:
        return {"verified": True, "confidence": prediction["rain_probability"]}
    
    return {"verified": False, "confidence": prediction["rain_probability"]}