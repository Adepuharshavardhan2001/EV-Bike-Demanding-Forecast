import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="EV / Bike Demand Forecaster",
    layout="wide"
)

st.title(" EV / Bike Demand Forecasting")

# ====================== LOAD MODELS ======================
@st.cache_resource
def load_models():
    ml_model = joblib.load("final_best_model.pkl")
    arima_model = joblib.load("arima_model.pkl")
    return ml_model, arima_model

model, arima_model = load_models()

# ====================== TABS ======================
tab1, tab2 = st.tabs([" ML Forecast (Random Forest)", " ARIMA Time-Series Forecast"])

# ====================== TAB 1: ML FORECAST ======================
with tab1:
    st.subheader("Predict Hourly Demand")
    st.caption("Using Random Forest model | Test RMSE: 69.89 | R²: 0.90")

    col1, col2 = st.columns(2)

    with col1:
        hr = st.slider("Hour of Day", 0, 23, 12)
        mnth = st.slider("Month", 1, 12, 6)
        temp = st.slider("Temperature (Normalized)", 0.0, 1.0, 0.5)
        hum = st.slider("Humidity (Normalized)", 0.0, 1.0, 0.5)

    with col2:
        workingday = st.selectbox("Working Day?", [1, 0], index=1)
        weathersit = st.selectbox(
            "Weather Situation",
            [1, 2, 3, 4],
            format_func=lambda x: ["Clear", "Mist/Cloudy", "Light Rain/Snow", "Heavy Rain/Snow"][x-1]
        )
        windspeed = st.slider("Wind Speed (Normalized)", 0.0, 1.0, 0.2)

    # Prepare input data
    input_data = pd.DataFrame([[
        1,          # season (placeholder)
        1,          # yr (placeholder)
        mnth,
        hr,
        0,          # holiday
        3,          # weekday (placeholder)
        workingday,
        weathersit,
        temp,
        temp,       # atemp
        hum,
        windspeed
    ]], columns=[
        'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday',
        'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed'
    ])

    if st.button(" Predict Demand", type="primary", use_container_width=True):
        with st.spinner("Predicting..."):
            prediction = model.predict(input_data)[0]
            
            st.success(f"**Predicted Ride Demand: {int(round(prediction)):,} rides**")
            
            # Additional insights
            if prediction > 300:
                st.info(" **High Demand** - Consider increasing fleet availability")
            elif prediction < 50:
                st.info(" **Low Demand** period")

# ====================== TAB 2: ARIMA FORECAST ======================
with tab2:
    st.subheader("ARIMA Daily Forecast")
    st.caption("Univariate Time Series Model")

    days = st.slider("Forecast Next N Days", min_value=1, max_value=60, value=30)
    
    if st.button("Generate ARIMA Forecast", type="primary"):
        with st.spinner("Generating forecast..."):
            forecast = arima_model.forecast(steps=days)
            
            # Plot
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=forecast.index,
                y=forecast,
                mode='lines+markers',
                name='Predicted Demand',
                line=dict(color='royalblue', width=3)
            ))
            
            fig.update_layout(
                title="ARIMA Daily Bike/EV Demand Forecast",
                xaxis_title="Date",
                yaxis_title="Predicted Ride Count",
                hovermode="x unified",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)

            # Show sample forecast
            st.dataframe(forecast.head(10).round(2), use_container_width=True)

