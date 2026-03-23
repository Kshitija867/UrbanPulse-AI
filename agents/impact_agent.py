def impact_agent(context):
    vendors = 450
    avg_loss = 800
    multiplier = context["multiplier"]

    var = vendors * avg_loss * multiplier

    return {
        "vendors": vendors,
        "avg_loss": avg_loss,
        "VaR": var
    }