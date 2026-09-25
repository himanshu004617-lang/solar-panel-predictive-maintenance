import os
import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Allow Python to find data_loader.py
sys.path.append(os.path.dirname(__file__))

from data_loader import load_datasets, create_dataframe


# --------------------------------------------------
# Load dataset
# --------------------------------------------------

electrical_data, environmental_data = load_datasets()

df = create_dataframe(
    electrical_data,
    environmental_data
)


# --------------------------------------------------
# Convert fault numbers to readable names
# --------------------------------------------------

fault_names = {
    0: "Normal",
    1: "Short Circuit",
    2: "Degradation",
    3: "Open Circuit",
    4: "Shadowing"
}

df["condition"] = df["f_nv"].map(fault_names)


# --------------------------------------------------
# 1. Fault distribution
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="condition",
    order=[
        "Normal",
        "Short Circuit",
        "Degradation",
        "Open Circuit",
        "Shadowing"
    ]
)

plt.title("Solar Panel Fault Distribution")
plt.xlabel("Operating Condition")
plt.ylabel("Number of Samples")
plt.xticks(rotation=20)

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 2. Irradiance vs Condition
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="condition",
    y="irr",
    order=[
        "Normal",
        "Short Circuit",
        "Degradation",
        "Open Circuit",
        "Shadowing"
    ]
)

plt.title("Irradiance Distribution by Solar Panel Condition")
plt.xlabel("Operating Condition")
plt.ylabel("Irradiance")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 3. PV Temperature vs Condition
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="condition",
    y="pvt",
    order=[
        "Normal",
        "Short Circuit",
        "Degradation",
        "Open Circuit",
        "Shadowing"
    ]
)

plt.title("PV Temperature Distribution by Condition")
plt.xlabel("Operating Condition")
plt.ylabel("PV Temperature")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 4. Voltage comparison
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="condition",
    y="vdc1",
    order=[
        "Normal",
        "Short Circuit",
        "Degradation",
        "Open Circuit",
        "Shadowing"
    ]
)

plt.title("DC Voltage Distribution by Condition")
plt.xlabel("Operating Condition")
plt.ylabel("DC Voltage")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 5. Current comparison
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="condition",
    y="idc1",
    order=[
        "Normal",
        "Short Circuit",
        "Degradation",
        "Open Circuit",
        "Shadowing"
    ]
)

plt.title("DC Current Distribution by Condition")
plt.xlabel("Operating Condition")
plt.ylabel("DC Current")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()