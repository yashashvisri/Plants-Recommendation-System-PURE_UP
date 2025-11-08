from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_recommendations")
def get_recommendations():
    try:
        # Replace with your API URL
        url = "https://fastapi-voting-based-model-api-for-plant.onrender.com/predict"

        # Simulated auto-fetch values
        auto_data = {
            "PM2_5": round(random.uniform(10, 100), 2),
            "PM10": round(random.uniform(10, 150), 2),
            "NO": round(random.uniform(5, 40), 2),
            "NO2": round(random.uniform(5, 40), 2),
            "NOx": round(random.uniform(10, 70), 2),
            "NH3": round(random.uniform(1, 10), 2),
            "CO": round(random.uniform(100, 300), 2),
            "SO2": round(random.uniform(5, 20), 2),
            "O3": round(random.uniform(10, 50), 2),
            "Benzene": round(random.uniform(1, 5), 2),
            "Toluene": round(random.uniform(5, 20), 2),
            "Xylene": round(random.uniform(1, 5), 2),
            "AQI": random.randint(0, 500)
        }

        res = requests.post(url, json=auto_data)
        if res.status_code == 200:
            return jsonify(res.json())
        else:
            return jsonify({"error": "API call failed"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
