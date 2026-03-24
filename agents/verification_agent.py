from utils.geo import calculate_distance

# def verification_agent(context):
#     rain_lat, rain_lon = context["coords"]
#     vendor_lat, vendor_lon = context["vendor_location"]

#     distance = calculate_distance(rain_lat, rain_lon, vendor_lat, vendor_lon)

#     #  Relaxed threshold imp
#     if distance > 10:   
#         return {"verified": False, "reason": "Rain too far from vendor location"}

#     return {"verified": True}

def verification_agent(context):
    rain = context.get("simulated_rain", 0)

    if rain > 5:
        return {"verified": True}
    else:
        return {"verified": False}