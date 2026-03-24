import json

def load_vendors():
    with open("data/vendors.json", "r") as f:
        return json.load(f)