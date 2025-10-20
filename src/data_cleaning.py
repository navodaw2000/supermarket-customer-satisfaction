# Step 1: Import libraries
import pandas as pd

# Step 2: Load the dataset
file_path = "data/raw/Form_Responses.csv"
df = pd.read_csv(file_path)

# Step 3: Quick overview of the data 
print("First 5 rows:")
print(df.head())
print("\nData info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 4: Rename columns for easier access
# Example: Overall Satisfaction → overall_satisfaction, Province → province
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

# Step 5: Handle missing values
# Option 1: Drop rows with missing values (if small dataset)
df = df.dropna()

# Option 2: Fill missing values (optional)
# df['overall_satisfaction'] = df['overall_satisfaction'].fillna(df['overall_satisfaction'].mean())

# Step 6: Remove duplicate rows
df = df.drop_duplicates()

# Step 7: Convert data types
# Example: convert ratings to numeric
df['overall_satisfaction'] = pd.to_numeric(df['overall_satisfaction'], errors='coerce')

# Step 8: Normalize text columns (optional)
# Example: province names to lowercase
if 'province' in df.columns:
    df['province'] = df['province'].str.strip().str.lower()

# Step 9: Verify cleaned data
print("\nCleaned Data Info:")
print(df.info())
print("\nFirst 5 rows of cleaned data:")
print(df.head())

# Step 10: Save cleaned dataset
df.to_csv("data/processed/responses_cleaned.csv", index=False)
print("\nCleaned data saved to data/processed/responses_cleaned.csv")

