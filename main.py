from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

competition_date_str = "2025-07-20"
competition_date_str = os.getenv("COMPETITION_DATE", competition_date_str)
competition_date = datetime.strptime(competition_date_str, "%Y-%m-%d")
responses = 0

@app.route("/status", methods=["GET"])
def get_status():
    today = datetime.now()
    days_left = (competition_date - today).days
    is_live = days_left <= 0

    return jsonify({
        "days_left": days_left,
        "is_live": is_live,
        "responses": responses,
        "competition_date": competition_date.strftime("%d %B")  # e.g., "20 July"
    })
