# src/ingest.py
import pandas as pd

# Replace with your Google Sheet CSV link
url = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/export?format=csv"

# Download and save locally
df = pd.read_csv(url)
df.to_csv("data/raw/supermarket_responses.csv", index=False)

print("Data downloaded and saved to data/raw/supermarket_responses.csv")
