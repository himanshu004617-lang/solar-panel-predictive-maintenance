import os
import joblib
import pandas as pd


# ==============================
# LOAD TRAINED MODEL
# ==============================

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(
    PROJECT_DIR,
    "models",
    "solar_fault_model.pkl"
)

model = joblib.load(MODEL_PATH)


# ==============================
# FAULT NAMES
# ==============================

fault_names = {
    0: "Normal",
    1: "Short Circuit",
    2: "Degradation",
    3: "Open Circuit",
    4: "Shadowing"
}


# ==============================
# PREDICTION FUNCTION
# ==============================

def predict_solar_condition(
    idc1,
    idc2,
    vdc1,
    vdc2,
    irr,
    pvt
):
    
    input_data = pd.DataFrame([{
        "idc1": idc1,
        "idc2": idc2,
        "vdc1": vdc1,
        "vdc2": vdc2,
        "irr": irr,
        "pvt": pvt
    }])

    prediction = model.predict(input_data)[0]

    condition = fault_names.get(
        int(prediction),
        "Unknown"
    )

    # ==============================
    # MAINTENANCE STATUS
    # ==============================

    if condition == "Normal":
        maintenance = "No maintenance required"
    else:
        maintenance = "Maintenance required"

    return condition, maintenance


# ==============================
# TEST THE PREDICTION SYSTEM
# ==============================

if __name__ == "__main__":

    condition, maintenance = predict_solar_condition(
        idc1=0.0608,
        idc2=0.0073,
        vdc1=0.7143,
        vdc2=0.5550,
        irr=1.3729,
        pvt=2.3816
    )

    print("\n========== SOLAR PANEL PREDICTION ==========")

    print("Predicted Condition:", condition)
    print("Maintenance Status:", maintenance)