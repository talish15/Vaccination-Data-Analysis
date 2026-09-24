# 📊 End-to-End Vaccination Data Pipeline & Streamlit Dashboard

An end-to-end data engineering and interactive visualization project. This repository extracts raw vaccination metrics, processes and cleans the data using Python and Pandas, loads the records into an SQLite database, and serves live analytical metrics via an interactive Streamlit web dashboard.

---

## 🏗️ Project Architecture
Vacation_Project/
├── app.py                      # Interactive Streamlit Web Application
├── data/
│   ├── raw_data.csv            # Original raw vaccination metrics
│   ├── cleaned_vaccination_data.csv # Preprocessed dataset
│   └── vaccination_db.db       # SQLite Database storage
├── scripts/
│   ├── data_cleaning.py        # Automated ETL/data cleaning script
│   ├── create_db.py            # SQLite database schema creation & ingestion
│   └── analyze_db.py           # SQL querying and aggregation functions
├── vaccination_summary.png     # Exported dashboard output preview
└── README.md                   # Project documentation
---

## Features & Pipeline Overview

1. **ETL Data Processing**: Cleans missing values, formats timestamps, and normalizes feature values using Pandas.
2. **Database Storage**: Creates tables and persists the cleaned data in an SQLite database using Python (`sqlite3`).
3. **Interactive Visualizations**: Displays total vaccination trends, regional breakdowns, and key KPI summaries using Streamlit and Plotly/Matplotlib.

---

## Getting Started Locally

### Prerequisites
- Python 3.8 or higher

### Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/talish15/Vaccination-Data-Analysis.git](https://github.com/talish15/Vaccination-Data-Analysis.git)
   cd Vaccination-Data-Analysis
   pip install pandas streamlit
   streamlit run app.py
