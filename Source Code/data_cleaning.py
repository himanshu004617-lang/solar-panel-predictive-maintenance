import os
import sys

import pandas as pd

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
# Basic dataset information
# --------------------------------------------------

print("\n========== DATASET INFORMATION ==========")

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())


# --------------------------------------------------
# Check fault labels
# --------------------------------------------------

print("\n========== FAULT LABELS ==========")

print("\nUnique values in f_nv:")

print(df["f_nv"].unique())


print("\nNumber of samples for each fault label:")

print(df["f_nv"].value_counts().sort_index())


# --------------------------------------------------
# Percentage of each class
# --------------------------------------------------

print("\n========== CLASS PERCENTAGE ==========")

class_percentage = (
    df["f_nv"]
    .value_counts(normalize=True)
    .sort_index()
    * 100
)

print(class_percentage)


# --------------------------------------------------
# Check duplicates
# --------------------------------------------------

print("\n========== DUPLICATES ==========")

print(
    "Number of duplicate rows:",
    df.duplicated().sum()
)


# --------------------------------------------------
# Statistical information
# --------------------------------------------------

print("\n========== STATISTICAL SUMMARY ==========")

print(df.describe())