import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# PostgreSQL Database Connection
DATABASE_URL = "postgresql://neondb_owner:QMz9xp1KiwOT@ep-round-surf-a1y04z36.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"

# Title of the Application
st.title("Weather and Air Quality Dashboard 🌦️")

# Sidebar for User Inputs
st.sidebar.header("Query Options")
table_choice = st.sidebar.selectbox("Select a Table:", ["weather_data", "air_quality_data", "merged_data"])
rows_limit = st.sidebar.slider("Number of Rows to Fetch:", min_value=5, max_value=100, value=10)

# Fetch Data from PostgreSQL
def fetch_data(table, limit):
    engine = create_engine(DATABASE_URL)
    query = f"SELECT * FROM {table} LIMIT {limit};"
    return pd.read_sql(query, con=engine)

# Display Data
st.header(f"Showing {rows_limit} rows from {table_choice}")
data = fetch_data(table_choice, rows_limit)
st.dataframe(data)

# Basic Statistics
if st.sidebar.checkbox("Show Data Statistics"):
    st.subheader("Data Statistics")
    st.write(data.describe())

# Visualization
if st.sidebar.checkbox("Show Temperature vs AQI Plot"):
    st.subheader("Temperature vs AQI")
    plt.figure(figsize=(10, 5))
    plt.scatter(data['temperature_celsius'], data['aqius'], c='blue')
    plt.xlabel('Temperature (Celsius)')
    plt.ylabel('AQI')
    plt.title('Temperature vs AQI Scatter Plot')
    st.pyplot(plt)

# Insert New Data (Optional)
st.sidebar.subheader("Insert New Data")
new_date = st.sidebar.text_input("Date (YYYY-MM-DD)")
new_temp = st.sidebar.number_input("Temperature (Celsius)", min_value=-50.0, max_value=50.0)
new_aqi = st.sidebar.number_input("AQI", min_value=0, max_value=500)

if st.sidebar.button("Insert Data"):
    engine = create_engine(DATABASE_URL)
    insert_query = f"""
    INSERT INTO merged_data (date, temperature_celsius, aqius) 
    VALUES ('{new_date}', {new_temp}, {new_aqi});
    """
    with engine.connect() as conn:
        conn.execute(insert_query)
        st.sidebar.success("✅ Data Inserted Successfully!")

# Footer
st.sidebar.text("Built with ❤️ using Streamlit")