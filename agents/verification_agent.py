from utils.geo import calculate_distance

def verification_agent(context):
    rain = context.get("simulated_rain", 0)

    if rain <= 5:
        return {"verified": False}

    # SAFE CHECK (only if coords exist)
    try:
        rain_lat, rain_lon = context["coords"]
        vendor_lat, vendor_lon = context["vendor_coords"]

        distance = calculate_distance(rain_lat, rain_lon, vendor_lat, vendor_lon)

        if distance > 5:
            return {"verified": False}

    except:
        pass  # fallback (no crash)

    return {"verified": True}