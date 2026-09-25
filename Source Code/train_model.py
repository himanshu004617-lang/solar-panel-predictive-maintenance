import os
import sys
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# --------------------------------------------------
# Allow Python to find data_loader.py
# --------------------------------------------------

sys.path.append(os.path.dirname(__file__))

from data_loader import load_datasets, create_dataframe


# --------------------------------------------------
# Load dataset
# --------------------------------------------------

print("Loading dataset...")

electrical_data, environmental_data = load_datasets()

df = create_dataframe(
    electrical_data,
    environmental_data
)


# --------------------------------------------------
# Features and target
# --------------------------------------------------

features = [
    "idc1",
    "idc2",
    "vdc1",
    "vdc2",
    "irr",
    "pvt"
]

X = df[features]

y = df["f_nv"]


print("\nFeatures:")
print(features)

print("\nTarget: f_nv")


# --------------------------------------------------
# Train/Test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# --------------------------------------------------
# Create Random Forest model
# --------------------------------------------------

print("\nTraining Random Forest...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)


# --------------------------------------------------
# Train model
# --------------------------------------------------

model.fit(X_train, y_train)


print("\nModel training completed!")


# --------------------------------------------------
# Create models directory
# --------------------------------------------------

PROJECT_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

MODEL_DIR = os.path.join(
    PROJECT_DIR,
    "models"
)

os.makedirs(
    MODEL_DIR,
    exist_ok=True
)


# --------------------------------------------------
# Save model
# --------------------------------------------------

model_path = os.path.join(
    MODEL_DIR,
    "solar_fault_model.pkl"
)

joblib.dump(
    model,
    model_path
)


print("\nModel saved successfully at:")

print(model_path)