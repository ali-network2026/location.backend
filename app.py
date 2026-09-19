from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Location backend is running."

@app.post("/location")
def location():
    data = request.get_json(silent=True) or {}

    latitude = data.get("latitude")
    longitude = data.get("longitude")
    accuracy = data.get("accuracy")

    if latitude is None or longitude is None:
        return jsonify({"ok": False}), 400

    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Accuracy:", accuracy)

    return jsonify({"ok": True})
