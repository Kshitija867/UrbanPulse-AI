from utils.api import get_weather

def ingestion_agent(location):
    lat, lon = location

    weather = get_weather(lat, lon)

    context = {
        "location": location,
        "precipitation": weather["precipitation"],
        "day_type": "weekend",  # you can improve later
        "multiplier": 1.5
    }

    return context