import os
import numpy as np
import pandas as pd
from scipy.io import loadmat


# --------------------------------------------------
# 1. Project paths
# --------------------------------------------------

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, "data")


electrical_file = os.path.join(DATA_DIR, "dataset_elec.mat")
environmental_file = os.path.join(DATA_DIR, "dataset_amb.mat")


# --------------------------------------------------
# 2. Load MATLAB files
# --------------------------------------------------

def load_datasets():

    print("Loading datasets...")

    electrical_data = loadmat(electrical_file)
    environmental_data = loadmat(environmental_file)

    return electrical_data, environmental_data


# --------------------------------------------------
# 3. Convert data into Pandas DataFrame
# --------------------------------------------------

def create_dataframe(electrical_data, environmental_data):

    data = {

        "idc1": np.ravel(electrical_data["idc1"]),
        "idc2": np.ravel(electrical_data["idc2"]),

        "vdc1": np.ravel(electrical_data["vdc1"]),
        "vdc2": np.ravel(electrical_data["vdc2"]),

        "irr": np.ravel(environmental_data["irr"]),
        "pvt": np.ravel(environmental_data["pvt"]),

        "f_nv": np.ravel(environmental_data["f_nv"])
    }

    df = pd.DataFrame(data)

    return df


# --------------------------------------------------
# 4. Main program
# --------------------------------------------------

if __name__ == "__main__":

    electrical_data, environmental_data = load_datasets()

    df = create_dataframe(
        electrical_data,
        environmental_data
    )

    print("\nDataset successfully converted to DataFrame!")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())