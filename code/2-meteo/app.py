from flask import Flask, jsonify, request
from flasgger import Swagger
import requests

app = Flask(__name__)
swagger = Swagger(app)

# Dictionnaire des villes connues avec leurs coordonnées
known_cities = {
    "Rodez": (44.35, 2.57),
    "Honolulu": (21.30, -157.85),
    "Tombouctou": (16.77, -3.01)
}

@app.route("/weather", methods=["GET"])
def get_weather():
    """
    Obtenir la météo actuelle pour une ville donnée
    ---
    parameters:
      - name: city
        in: query
        type: string
        required: true
        example: Rodez
    responses:
      200:
        description: Météo trouvée
        examples:
          application/json: {"city": "Rodez", "temperature": 21.3, "windspeed": 15.2, "condition": "partiellement nuageux"}
      400:
        description: Ville inconnue
    """
    city = request.args.get("city")
    if city not in known_cities:
        return jsonify({"error": "Ville inconnue"}), 400

    lat, lon = known_cities[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url).json()

    weather = response.get("current_weather", {})
    return jsonify({
        "city": city,
        "temperature": weather.get("temperature"),
        "windspeed": weather.get("windspeed"),
        "condition": "voir API"  # open-meteo ne donne pas directement l'état en texte
    })

@app.route("/cities", methods=["GET"])
def get_cities():
    """
    Liste des villes supportées
    ---
    responses:
      200:
        description: Liste des villes
        examples:
          application/json: {"available_cities": ["Rodez", "Honolulu", "Tombouctou"]}
    """
    return jsonify({"available_cities": list(known_cities.keys())})

if __name__ == "__main__":
    app.run(debug=True)
