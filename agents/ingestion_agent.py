from utils.api import get_weather
def ingestion_agent(location, simulated_rain=None):
    if simulated_rain is not None:
        rain = simulated_rain
    else:
        from utils.api import get_weather
        lat, lon = location
        weather = get_weather(lat, lon)
        rain = weather["precipitation"]

    context = {
        "location": location,
        "precipitation": rain,
        "day_type": "weekend",
        "multiplier": 1.5
    }

    return context
# def ingestion_agent(location):
#     lat, lon = location

#     weather = get_weather(lat, lon)

#     context = {
#         "location": location,
#         "precipitation": weather["precipitation"],
#         "day_type": "weekend",  # you can improve later
#         "multiplier": 1.5
#     }

#     return context