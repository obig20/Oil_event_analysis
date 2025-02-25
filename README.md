Explanation of the Program
Task 1: Defining the Workflow
Steps: The program outlines a clear workflow: data collection, preprocessing, EDA, modeling, evaluation, and insights.
Data Understanding: It explains that Brent oil prices are daily market data, subject to gaps (e.g., weekends), and compiled by agencies like the EIA.
Model: Focuses on ARIMA as a starting point, describing inputs (prices), parameters (p, d, q), and outputs (forecasts).
Assumptions: Notes stationarity assumptions and limitations like missing external shocks.
Communication: Suggests reports and visualizations for stakeholders.
Task 1: Understanding Models and Data
ARIMA: Chosen for its simplicity in univariate time series analysis, with notes on its purpose (forecasting) and limitations (linearity).
Data Process: Prices reflect supply/demand dynamics, modeled as a time series.
Implementation
Data: Uses your sample Brent oil prices, preprocessed with pd.to_datetime(), set_index(), and asfreq('D').ffill() to ensure daily frequency.
EDA: Visualizes the price trend.
ARIMA: Fits a basic ARIMA(1,1,1) model, forecasts 5 days, and evaluates with RMSE.
Output: Plots actual vs. forecasted prices.
Task 2: Adapting Knowledge
Advanced Models: Suggests VAR, Markov-Switching ARIMA, and LSTM for future expansion.
External Factors: Introduces a placeholder for GDP data, with plans to include inflation, tech changes, etc.
Validation: Notes backtesting and cross-validation for future steps.