import pandas as pd
import os

INPUT_PATH = "data/full_data.csv"
OUTPUT_PATH = "data/cleaned_data.csv"

def clean_dataset():
    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(f"Cannot find input file: {INPUT_PATH}")

    df = pd.read_csv(INPUT_PATH)
    print(f"Loaded data: {df.shape}")

    # Drop columns that are mostly empty (>50% missing)
    limit = len(df) * 0.5
    df_clean = df.dropna(thresh=limit, axis=1)
    
    dropped = set(df.columns) - set(df_clean.columns)
    print(f"Dropped {len(dropped)} columns due to excessive missing values")

    # Fill remaining missing values
    # Median for numbers, Mode for categorical stuff
    nums = df_clean.select_dtypes(include=['number']).columns
    cats = df_clean.select_dtypes(include=['object']).columns

    for c in nums:
        if df_clean[c].isnull().any():
            df_clean[c] = df_clean[c].fillna(df_clean[c].median())

    for c in cats:
        if df_clean[c].isnull().any():
            top = df_clean[c].mode()[0]
            df_clean[c] = df_clean[c].fillna(top)

    # double check
    remaining = df_clean.isnull().sum().sum()
    print(f"Missing values after cleanup: {remaining}")
    print(f"Final shape: {df_clean.shape}")

    df_clean.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    clean_dataset()
