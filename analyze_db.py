import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Define paths relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "data", "vaccination_db.db")
# 2. Connect to SQLite database
conn = sqlite3.connect(db_path)

# 3. Query: Vaccination summary and dropoff rate by country
query = """
SELECT 
    country,
    SUM(dose_1) AS total_dose_1,
    SUM(dose_2) AS total_dose_2,
    SUM(total_doses) AS grand_total_doses,
    AVG(dropoff_rate_pct) AS avg_dropoff_rate
FROM vaccination_records
GROUP BY country
ORDER BY grand_total_doses DESC;
"""

df_summary = pd.read_sql_query(query, conn)
conn.close()

# 4. Display terminal results
print("--- Vaccination Summary ---")
print(df_summary.to_string(index=False))

# 5. Generate and save a summary chart
plt.figure(figsize=(8, 5))
sns.barplot(data=df_summary, x='country', y='grand_total_doses', palette='Blues_d')
plt.title('Total Vaccination Doses Administered by Country')
plt.xlabel('Country')
plt.ylabel('Total Doses')
plt.tight_layout()

# Save plot to data directory
chart_path = os.path.join(script_dir, "..", "data", "vaccination_summary.png")
plt.savefig(chart_path)
print(f"\nChart saved successfully to: {chart_path}")
