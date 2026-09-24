import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Locate CSV file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Check if CSV is in root or inside a /data folder
csv_path = os.path.join(script_dir, "country_vaccinations.csv")
if not os.path.exists(csv_path):
    csv_path = os.path.join(script_dir, "data", "country_vaccinations.csv")

# 2. Read dataset
df = pd.read_csv(csv_path)

# 3. Streamlit Dashboard Layout
st.title("Vaccination Data Dashboard")

st.subheader("Dataset Summary")
st.dataframe(df.head())

# 4. Visualization
st.subheader("Total Vaccinations Overview")
fig, ax = plt.subplots(figsize=(8, 5))
if 'country' in df.columns and 'total_vaccinations' in df.columns:
    summary_df = df.groupby('country')['total_vaccinations'].max().reset_index().dropna()
    summary_df = summary_df.sort_values(by='total_vaccinations', ascending=False).head(10)
    sns.barplot(data=summary_df, x='country', y='total_vaccinations', palette='Blues_d', ax=ax)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.write("Summary chart metrics not found in columns.")
