# src/clean_nav_history.py

import pandas as pd

df = pd.read_csv("../data/raw/02_nav_history.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
df = df.drop_duplicates()

# Validate NAV
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV records:", len(invalid_nav))

# Forward fill NAV per scheme
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

df.to_csv(
    "../data/processed/nav_history_clean.csv",
    index=False
)

print("Saved nav_history_clean.csv")
