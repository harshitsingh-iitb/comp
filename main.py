from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Example competition details
competition_date = datetime(2025, 7, 20)
responses = 134  # Replace with dynamic data if needed

@app.route("/status", methods=["GET"])
def get_status():
    today = datetime.now()
    days_left = (competition_date - today).days
    is_live = days_left <= 0

    return jsonify({
        "days_left": days_left,
        "is_live": is_live,
        "responses": responses
    })

if __name__ == "__main__":
    app.run(debug=True)