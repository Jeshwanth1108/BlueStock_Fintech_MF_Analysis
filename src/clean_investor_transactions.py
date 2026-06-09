import pandas as pd

df = pd.read_csv(
    "../data/raw/08_investor_transactions.csv"
)

# Date conversion
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction types
mapping = {
    "sip":"SIP",
    "SIP":"SIP",
    "lumpsum":"Lumpsum",
    "redemption":"Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
      .astype(str)
      .str.lower()
      .map(mapping)
)

# Amount validation
invalid_amounts = df[df["amount_inr"] <= 0]

print(
    "Invalid Amount Records:",
    len(invalid_amounts)
)

# KYC validation
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

print(
    df[~df["kyc_status"].isin(valid_kyc)]
)

df.to_csv(
    "../data/processed/investor_transactions_clean.csv",
    index=False
)