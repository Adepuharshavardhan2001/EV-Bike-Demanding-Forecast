# EV & Bike Demand Forecasting

A professional-grade forecasting platform that combines Supervised Machine Learning (Random Forest) with Statistical Time-Series (ARIMA) to predict urban mobility demand.
This tool provides both granular hourly predictions and long-term daily trends through an interactive Streamlit interface.

 # Application Features:

Hourly ML Predictor: Uses a trained Random Forest pipeline to predict specific ride counts based on weather and time variables (R2 = 0.90).

Daily ARIMA Forecast: Projects total ride volume for the next 60 days using univariate time-series analysis.

Automated Pipeline: Full preprocessing (OneHotEncoding + Scaling) bundled into a single joblib file for zero-latency deployment.

Interactive Dashboard: A "What-If" analysis tool to see how humidity, temperature, and work schedules impact fleet demand.

# The Machine Learning Pipeline:

# Exploratory Data Analysis (EDA)

Distribution: Identified right-skewed demand patterns using Seaborn KDE plots.

Correlation: Analyzed environmental impacts; found atemp (feeling temperature) to be the strongest positive driver and humidity the strongest negative driver.

Temporal Splits: Implemented a non-random 80/20 time-based split to ensure the model generalizes to the future, not just the past.

# 2. Model Benchmarking

I compared multiple architectures to find the most efficient predictor:

<img width="305" height="174" alt="image" src="https://github.com/user-attachments/assets/785feb8a-92b9-42ef-ab5b-bf1f7915d95f" />
