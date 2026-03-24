import requests

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=precipitation"

    response = requests.get(url)
    data = response.json()

    return {
        "precipitation": data["current"]["precipitation"]
    }