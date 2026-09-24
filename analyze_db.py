import os
import pandas as pd
import sqlite3

# Define relative paths
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "data", "country_vaccinations.csv")
db_path = os.path.join(script_dir, "data", "vaccination_db.db")

# Read CSV and populate SQLite database
df = pd.read_csv(csv_path)
conn = sqlite3.connect(db_path)
df.to_sql("vaccination_records", conn, if_exists="replace", index=False)
conn.close()
