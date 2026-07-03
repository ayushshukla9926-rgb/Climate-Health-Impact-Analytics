
import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/global_climate_health_impact_tracker_2015_2025.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"]).dt.date

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check data types
print("\nData Types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("data/processed/climate_health_cleaned.csv", index=False)

print("\n✅ Data cleaning completed successfully!")