from flask import Flask, render_template, request
import numpy as np
import pickle
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb

app = Flask(__name__)

models_dir = "Stock-Price-Prediction/prediction.pkl"
data_file = "Stock-Price-Prediction/Updated_SBIN.csv"

df = pd.read_csv(data_file)
print(df.columns)

# Load the model
try:
    with open(models_dir, "rb") as stock_file:
        stock_model = pickle.load(stock_file)
except FileNotFoundError:
    stock_model = None

def save_data(inputs, close_prediction):
    new_data = pd.DataFrame([inputs + [close_prediction]], columns=['Open', 'High', 'Low', 'Volume', 'Close'])
    with open(data_file, mode='a', newline='') as file:
        new_data.to_csv(file, header=False, index=False)

def retrain_model():
    X = df[['Open', 'High', 'Low', 'Volume']]
    y = df['Close']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    stock_model_xgb = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
    stock_model_xgb.fit(X_train, y_train)

    with open(models_dir, "wb") as stock_file_xgb:
        pickle.dump(stock_model_xgb, stock_file_xgb)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_close', methods=['GET', 'POST'])
def predict_close():
    if request.method == 'POST':
        try:
            inputs = [
                float(request.form.get('Open')),
                float(request.form.get('High')),
                float(request.form.get('Low')),
                float(request.form.get('Volume'))
            ]

            close_prediction = stock_model.predict(np.array([inputs]))[0] if stock_model else None

            save_data(inputs, close_prediction)
            retrain_model()

            return str(round(close_prediction, 2)) if close_prediction is not None else "Error: Stock model not loaded."
        except Exception as e:
            return f"An error occurred: {e}"
    # If it's a GET request, render the stock.html page
    return render_template('stock.html')

if __name__ == "__main__":
    app.run(debug=True)
