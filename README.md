# EV / Bike Demand Forecasting Platform

An end-to-end Machine Learning and Time-Series forecasting platform built to predict urban EV/Bike demand using Random Forest Regression and ARIMA forecasting.

The project includes:
- Hourly ride demand prediction
- Long-term demand forecasting
- Interactive Streamlit dashboard
- Business-oriented demand insights

---

## Application Preview

### Streamlit Dashboard
![Dashboard](images/dashboard.png)

---

## Business Problem

Urban mobility platforms require accurate demand forecasting to:
- optimize fleet availability
- reduce idle vehicles
- improve customer availability
- plan operational resources efficiently

This project predicts ride demand using weather, seasonal, and temporal variables.

---

## Features

- Random Forest hourly demand prediction
- ARIMA-based future forecasting
- Interactive Streamlit UI
- “What-If” scenario analysis
- Automated preprocessing pipeline
- Business demand recommendations

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- ARIMA (statsmodels)
- Plotly
- Matplotlib
- Seaborn

---

## Project Workflow

Data Collection → EDA → Feature Engineering → Model Building → Model Comparison → ARIMA Forecasting → Streamlit Deployment

---

## Dataset

- Source: Bike Sharing Dataset
- Records: 17,379 hourly observations

### Features:
- weather
- humidity
- temperature
- working day
- hour
- season

---

## Exploratory Data Analysis

### Demand Distribution
![Distribution](images/distribution.png)

### Correlation Heatmap
![Heatmap](images/heatmap.png)

---

## Model Performance

| Model | RMSE | R² Score |
|------|------|------|
| Random Forest | 69.89 | 0.90 |
| Gradient Boosting | 91.67 | 0.83 |
| Linear Regression | 203.04 | 0.15 |
| ARIMA (5,1,2) | Time-Series | Forecasting |

---

## Best Model

Random Forest achieved the best performance with:
- RMSE: 69.89
- R² Score: 0.90

### Important Features
- Feeling Temperature
- Evening Peak Hours
- Humidity
- Working Day

---

## Streamlit Application

The application allows users to:
- predict hourly demand
- simulate weather conditions
- generate ARIMA forecasts
- analyze mobility demand interactively

---

## Future Improvements

- Real-time API integration
- LSTM forecasting models
- Cloud deployment
- Live weather integration
- Dynamic traffic analysis

---

## Author

### A. Harshavardhan

- LinkedIn: https://www.linkedin.com/in/adepu-harshavardhan-ds/
- GitHub: https://github.com/Adepuharshavardhan2001
