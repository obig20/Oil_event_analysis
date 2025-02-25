from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Load your dataset
df_path = r"C:\Users\h\Desktop\week 10\Data\BrentOilPrices.csv"

# Check if the file exists and is not empty
if os.path.exists(df_path) and os.path.getsize(df_path) > 0:
    # Load the CSV file
    data = pd.read_csv(df_path, parse_dates=['Date'], index_col='Date')
    data.reset_index(inplace=True)
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')  # Convert dates to strings for JSON serialization
else:
    print("Error: The file does not exist or is empty.")
    data = pd.DataFrame()  # Create an empty DataFrame to avoid further errors

# API to get all data
@app.route('/api/data', methods=['GET'])
def get_data():
    if data.empty:
        return jsonify({"error": "No data available"}), 404
    return jsonify(data.to_dict(orient='records'))

# API to filter data by date range
@app.route('/api/filter', methods=['GET'])
def filter_data():
    if data.empty:
        return jsonify({"error": "No data available"}), 404

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({"error": "Please provide both start_date and end_date"}), 400

    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
    return jsonify(filtered_data.to_dict(orient='records'))

# API to get specific columns (e.g., Price, Returns, Volatility)
@app.route('/api/columns', methods=['GET'])
def get_columns():
    if data.empty:
        return jsonify({"error": "No data available"}), 404

    columns = request.args.get('columns', 'Price').split(',')
    filtered_data = data[['Date'] + columns]
    return jsonify(filtered_data.to_dict(orient='records'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)