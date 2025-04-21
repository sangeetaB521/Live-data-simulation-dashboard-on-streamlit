# Updated Streamlit Code with Fix
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import streamlit as st
import joblib
import time

# Load your trained model
model_path = "cosstorerev_model.pkl"
try:
    model = joblib.load(model_path)
    model_columns = model.feature_names_in_
except FileNotFoundError:
    st.error("Model file not found! Please provide a valid path.")
    model = None
    model_columns = []

# Simulating dataset
def simulate_data(n_samples=100):
    start_date = datetime.now() - timedelta(days=30)
    data = pd.DataFrame({
        'Time_of_purchase': [start_date + timedelta(days=np.random.randint(0, 30)) for _ in range(n_samples)],
        'Product_category': [random.choice(['Skincare', 'Makeup', 'Haircare', 'Bodycare']) for _ in range(n_samples)],
        'Product_price': [round(random.uniform(500, 5000), 2) for _ in range(n_samples)],
        'Quantity': [random.randint(1, 5) for _ in range(n_samples)],
        'Membership': [random.choice(['Premium', 'Gold', 'Starter']) for _ in range(n_samples)],
        'Platform_used': [random.choice(['Website', 'Quickcom', 'Offline', 'ecom']) for _ in range(n_samples)]
    })
    return data

# Preprocessing dataset
def preprocess_data(data):
    data = pd.get_dummies(
        data,
        columns=['Product_category', 'Membership', 'Platform_used'],
        drop_first=True
    )
    for col in model_columns:
        if col not in data.columns:
            data[col] = 0
    data = data[model_columns]
    return data

# Initialize live_data
live_data = pd.DataFrame()

# Streamlit App Layout
st.title("Lavender Lifestyle Store")
st.subheader("Real-Time Revenue Predictions Dashboard")

# Simulation Speed
simulation_speed = st.slider("Simulation Speed (seconds per batch)", 1, 5, 2)

# Information Section
if st.button("Show Information"):
    st.info("""
    ### How This Works
    - **Predicted Revenue**: Generated using a trained ML model based on features like product category, price, membership, and platform used.
    - **Real-Time Updates**: The dashboard simulates and processes live data for revenue predictions.
    """)

# Real-Time Simulation and Visualization
st.subheader("Real-Time Data and Predictions")

if st.button("Start Simulation"):
    for i in range(10):  # Simulating 10 batches
        new_data = simulate_data(n_samples=10)
        new_data["Time_of_purchase"] = new_data["Time_of_purchase"].dt.strftime("%Y-%m-%d %H:%M:%S")
        processed_new_data = preprocess_data(new_data)
        if model:
            new_data["Predicted_Revenue"] = model.predict(processed_new_data)
        else:
            new_data["Predicted_Revenue"] = np.nan
        
        live_data = pd.concat([live_data, new_data], ignore_index=True)
        st.write(live_data.tail(10))  # Show the latest 10 rows
        
        # Real-Time Line Chart
        st.line_chart(live_data.set_index("Time_of_purchase")["Predicted_Revenue"])
        
        # Wait for simulation speed
        time.sleep(simulation_speed)

# Bar Chart for Aggregate Metrics
if not live_data.empty:
    st.subheader("Aggregate Metrics")
    agg_data = live_data.groupby("Product_category")["Predicted_Revenue"].mean().reset_index()
    st.bar_chart(agg_data.set_index("Product_category"))





