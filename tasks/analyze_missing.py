import pandas as pd
import os

def analyze():
    fpath = "data/full_data.csv"
    
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        return

    df = pd.read_csv(fpath)
    
    with open("missing_report.txt", "w", encoding="utf-8") as f:
        f.write("\n--- Dataset Info ---\n")
        df.info(buf=f)

        nulls = df.isnull().sum()
        
        f.write("\n--- Missing Values ---\n")
        f.write(nulls[nulls > 0].to_string())

        # calculate percentages
        pct = (nulls / len(df)) * 100
        f.write("\n\n--- Missing Percents ---\n")
        f.write(pct[pct > 0].to_string())
        
    print("Analysis complete. Saved to missing_report.txt")

if __name__ == "__main__":
    analyze()
