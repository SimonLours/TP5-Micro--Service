from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from models import db, WeatherData
import requests
from datetime import datetime, timedelta
import os

app = Flask(__name__)
swagger = Swagger(app)

# Configuration SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

known_cities = {
    "Rodez": (44.35, 2.57),
    "Honolulu": (21.30, -157.85),
    "Tombouctou": (16.77, -3.01)
}

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if city not in known_cities:
        return jsonify({"error": "Ville inconnue"}), 400

    # Vérifier si une entrée récente existe en BDD (moins de 10 minutes)
    entry = WeatherData.query.filter_by(city=city).order_by(WeatherData.timestamp.desc()).first()
    if entry and entry.timestamp > datetime.utcnow() - timedelta(minutes=10):
        return jsonify({
            "city": city,
            "temperature": entry.temperature,
            "windspeed": entry.windspeed,
            "condition": entry.condition
        })

    lat, lon = known_cities[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    data = requests.get(url).json().get("current_weather", {})

    new_entry = WeatherData(
        city=city,
        temperature=data.get("temperature"),
        windspeed=data.get("windspeed"),
        condition="voir API",
        timestamp=datetime.utcnow()
    )
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({
        "city": city,
        "temperature": new_entry.temperature,
        "windspeed": new_entry.windspeed,
        "condition": new_entry.condition
    })

@app.route("/cities", methods=["GET"])
def get_cities():
    return jsonify({"available_cities": list(known_cities.keys())})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
