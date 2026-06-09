import pandas as pd
import os

INPUT_FILE = "../data/raw/10_benchmark_indices.csv"
OUTPUT_FILE = "../data/processed/benchmark_indices_clean.csv"

df = pd.read_csv(INPUT_FILE)

print("="*60)
print("DATA CLEANING")
print("="*60)

print("Original Shape:", df.shape)

# Remove duplicates
duplicates = df.duplicated().sum()
print("Duplicates:", duplicates)

df = df.drop_duplicates()

# Trim text columns
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Save
os.makedirs("../data/processed", exist_ok=True)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nSaved:", OUTPUT_FILE)
print("Final Shape:", df.shape)