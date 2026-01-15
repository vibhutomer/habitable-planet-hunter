import pandas as pd
import os

CLEAN_FILE = "data/cleaned_data.csv"
RAW_FILE = "data/full_data.csv"

def verify():
    if not os.path.exists(CLEAN_FILE):
        print(f"Error: {CLEAN_FILE} is missing")
        return

    df = pd.read_csv(CLEAN_FILE)
    
    # ensure no nulls left
    if df.isnull().sum().sum() == 0:
        print("PASS: Cleaned data has no missing values.")
    else:
        print("FAIL: Cleaned data still has missing values!")

    # make sure we actually dropped the bad columns
    raw = pd.read_csv(RAW_FILE)
    raw_missing = raw.isnull().sum() / len(raw)
    bad_cols = raw_missing[raw_missing > 0.5].index

    # check intersection
    still_present = [c for c in bad_cols if c in df.columns]
    
    if not still_present:
        print("PASS: High-missing columns were dropped.")
    else:
        print(f"FAIL: Found columns that should've been dropped: {still_present}")

    print(f"Final Verified Shape: {df.shape}")

if __name__ == "__main__":
    verify()
