from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

JOKES_SERVICE_URL = "http://jokes:5000/joke"
WEATHER_SERVICE_URL = "http://weather:5000/weather"

@app.route("/joke", methods=["GET"])
def get_joke():
    try:
        r = requests.get(JOKES_SERVICE_URL)
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": "Service blague indisponible"}), 503

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    try:
        r = requests.get(f"{WEATHER_SERVICE_URL}?city={city}")
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": "Service météo indisponible"}), 503

@app.route("/fullinfo", methods=["GET"])
def get_fullinfo():
    city = request.args.get("city")
    try:
        weather_resp = requests.get(f"{WEATHER_SERVICE_URL}?city={city}")
        weather_data = weather_resp.json()
    except:
        weather_data = {"error": "Service météo indisponible"}

    try:
        joke_resp = requests.get(JOKES_SERVICE_URL)
        joke_data = joke_resp.json().get("joke", "Pas de blague dispo.")
    except:
        joke_data = "Service blague indisponible"

    return jsonify({
        "city": city,
        "weather": weather_data if isinstance(weather_data, dict) else {},
        "joke": joke_data
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
