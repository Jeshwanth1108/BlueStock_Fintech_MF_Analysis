import pandas as pd
import os

RAW_PATH = "../data/raw"

files = sorted(
    [f for f in os.listdir(RAW_PATH)
     if f.endswith(".csv")]
)

print("="*80)
print("DATA INGESTION REPORT")
print("="*80)

for file in files:

    print("\n")
    print("="*80)
    print(file)
    print("="*80)

    df = pd.read_csv(os.path.join(RAW_PATH,file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Records:")
    print(df.head())