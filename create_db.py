import os
import sqlite3
import pandas as pd

# Define relative paths
# Define paths relative to this script's folder
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "..", "data", "cleaned_vaccination_data.csv")
db_path = os.path.join(script_dir, "..", "data", "vaccination_db.db")

# Read cleaned CSV
df = pd.read_csv(csv_path)

# Connect to SQLite and write table
conn = sqlite3.connect(db_path)
df.to_sql("vaccination_records", conn, if_exists="replace", index=False)

print(f"Database successfully created at: {db_path}")
conn.close()
