def decision_agent(impact):
    var = impact["VaR"]

    if var > 500000:
        return {"action": "PAYOUT", "amount": 250000}
    elif var > 200000:
        return {"action": "ALERT", "amount": 0}
    else:
        return {"action": "MONITOR", "amount": 0}