import os
import numpy as np
import pandas as pd

# Set paths relative to the scripts folder
input_path = os.path.join("..", "data", "raw_data.csv")
output_path = os.path.join("..", "data", "cleaned_vaccination_data.csv")

# Create sample raw dataset if raw_data.csv does not exist yet
if not os.path.exists(input_path):
    os.makedirs(os.path.dirname(input_path), exist_ok=True)
    sample_data = {
        "Country": [
            "India",
            "India",
            "USA",
            "USA",
            "Brazil",
            "Brazil",
            "UK",
            "UK",
        ],
        "Date": [
            "2023-01-01",
            "2023-01-08",
            "2023-01-01",
            "2023-01-08",
            "2023-01-01",
            "2023-01-08",
            "2023-01-01",
            "2023-01-08",
        ],
        "Vaccine Name": [
            "Covishield",
            "Covishield",
            "mRNA-1273",
            "mRNA-1273",
            "ChAdOx1",
            "ChAdOx1",
            "BNT162b2",
            "BNT162b2",
        ],
        "Dose 1": [5000, 5200, 4000, 4100, 3000, 3100, 2500, 2600],
        "Dose 2": [4200, 4500, 3800, 3900, 2100, 2300, 2200, 2400],
        "Disease Cases": [1200, 1100, 800, 750, 1500, 1400, 600, 550],
    }
    pd.DataFrame(sample_data).to_csv(input_path, index=False)
    print("Created initial dataset at data/raw_data.csv")

# Load data
df = pd.read_csv(input_path)

# Clean column headers
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Format date column
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])

# Calculate metrics
df["total_doses"] = df["dose_1"] + df["dose_2"]
df["dropoff_rate_pct"] = (
    (df["dose_1"] - df["dose_2"]) / df["dose_1"]
) * 100

# Save output
df.to_csv(output_path, index=False)
print(f"Data cleaned successfully! Saved to: {output_path}")
