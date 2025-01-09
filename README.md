# 🌦️ ETL Pipeline for Weather and Air Quality Analytics using Streamlit and PostgreSQL

---

## 📖 Project Overview
This project implements a complete **ETL (Extract, Transform, Load)** pipeline for **weather and air quality analytics**. It automates data collection from **VisualCrossing API** and **IQAir API**, cleans the data, stores it in a **Neon PostgreSQL** database, and visualizes the insights using an interactive **Streamlit** web dashboard.

---


## 📦 Technology Stack
- **Programming Language:** Python  
- **Frontend:** Streamlit  
- **Database:** Neon PostgreSQL (Cloud-hosted)  
- **APIs:** VisualCrossing API (Weather) | IQAir API (Air Quality)  
- **Python Libraries:** Pandas, SQLAlchemy, Psycopg2, Matplotlib, Requests  
- **Environment:** Google Colab and Local Virtual Environment (`venv`)  

---

## 📊 Project Architecture (ETL Workflow)
```plaintext
1. Extract: Fetch weather and air quality data from APIs using `requests`.
2. Transform: Clean data (NaN handling, unit conversions, flattening nested JSON).
3. Load: Store data into a cloud-hosted Neon PostgreSQL database using `SQLAlchemy`.
4. Visualize: Use Streamlit to create an interactive dashboard for insights.
