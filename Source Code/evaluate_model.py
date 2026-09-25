import os
import sys
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.dirname(__file__))
from data_loader import load_datasets, create_dataframe


# ==============================
# LOAD DATASET
# ==============================

print("Loading dataset...")

electrical_data, environmental_data = load_datasets()
df = create_dataframe(electrical_data, environmental_data)


# ==============================
# FEATURES AND TARGET
# ==============================

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


# ==============================
# CREATE SAME TRAIN/TEST SPLIT
# ==============================

print("\nCreating test dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==============================
# LOAD TRAINED MODEL
# ==============================

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(
    PROJECT_DIR,
    "models",
    "solar_fault_model.pkl"
)

print("\nLoading trained model...")

model = joblib.load(MODEL_PATH)


# ==============================
# PREDICT ONLY ON TEST DATA
# ==============================

print("\nMaking predictions on unseen test data...")

y_pred = model.predict(X_test)


# ==============================
# ACCURACY
# ==============================

accuracy = accuracy_score(y_test, y_pred)

print("\n========== TEST DATA ACCURACY ==========")

print(f"Accuracy: {accuracy:.4f}")
print(f"Accuracy percentage: {accuracy * 100:.2f}%")


# ==============================
# CLASSIFICATION REPORT
# ==============================

class_names = [
    "Normal",
    "Short Circuit",
    "Degradation",
    "Open Circuit",
    "Shadowing"
]

print("\n========== CLASSIFICATION REPORT ==========")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=class_names
    )
)


# ==============================
# CONFUSION MATRIX
# ==============================

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(9, 7))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=class_names,
    yticklabels=class_names
)

plt.title("Solar Panel Fault Classification - Confusion Matrix")
plt.xlabel("Predicted Condition")
plt.ylabel("Actual Condition")

plt.tight_layout()
plt.show()