from flask import Flask, render_template, request, jsonify
import sys
import os

# Allow Python to find files inside Source Code
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
SOURCE_CODE_DIR = os.path.join(PROJECT_DIR, "Source Code")

sys.path.append(SOURCE_CODE_DIR)

from prediction import predict_solar_condition


app = Flask(__name__)


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():
    return render_template("dashboard.html")


# ==============================
# PREDICTION API
# ==============================

@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        idc1 = float(data["idc1"])
        idc2 = float(data["idc2"])
        vdc1 = float(data["vdc1"])
        vdc2 = float(data["vdc2"])
        irr = float(data["irr"])
        pvt = float(data["pvt"])

        condition, maintenance = predict_solar_condition(
            idc1,
            idc2,
            vdc1,
            vdc2,
            irr,
            pvt
        )

        return jsonify({
            "condition": condition,
            "maintenance": maintenance
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 400


# ==============================
# RUN FLASK APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )