import pandas as pd
import os

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return {
        "stress": df["stress"].mean(),
        "mood": df["mood"].mean(),
        "sleep": df["sleep"].mean(),
        "notes": " ".join(df["note"].astype(str))
    }

def list_sample_csvs(directory="assets/samples"):
    return [
        f for f in os.listdir(directory)
        if f.endswith(".csv")
    ]
