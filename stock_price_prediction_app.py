import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from sklearn.preprocessing import MinMaxScaler
import xgboost as xgb
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.impute import SimpleImputer

# Load and preprocess the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('SBIN.csv')
    df.drop(['Date', 'Adj Close'], axis=1, inplace=True)  # Drop irrelevant columns

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    # Calculate VWAP
    df['VWAP'] = (df['Close'] * df['Volume']).cumsum() / df['Volume'].cumsum()

    return df

# Train the models
def train_models(df):
    # Select features and target variable
    X = df[['Open', 'High', 'Low', 'Volume', 'VWAP']]
    y = df['Close']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    models = {
        'Linear Regression': LinearRegression(),
        'SVR': SVR(),
        'Random Forest': RandomForestRegressor(),
        'Gradient Boosting': GradientBoostingRegressor(),
        'XGBoost': xgb.XGBRegressor(),
        'AdaBoost': AdaBoostRegressor(),
        'Decision Tree': DecisionTreeRegressor(),
        'KNeighbors': KNeighborsRegressor()
    }

    trained_models = {}
    
    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        trained_models[name] = model
    
    return trained_models, scaler, X_test_scaled, y_test

# Load data and train models
df = load_data()
trained_models, scaler, X_test_scaled, y_test = train_models(df)

# Streamlit app layout
st.title("Stock Price Prediction App")

# User input for stock features
open_price = st.number_input("Open Price:", min_value=0.0, format="%.2f")
high_price = st.number_input("High Price:", min_value=0.0, format="%.2f")
low_price = st.number_input("Low Price:", min_value=0.0, format="%.2f")
volume = st.number_input("Volume:", min_value=0, format="%d")

# Calculate VWAP for user input
vwap = (open_price + high_price + low_price) / 3  # Simplified VWAP calculation

# Dropdown for model selection
model_selection = st.selectbox("Select Model for Prediction:", options=list(trained_models.keys()))

# Button to predict
if st.button("Predict Closing Price"):
    input_data = np.array([[open_price, high_price, low_price, volume, vwap]])
    input_scaled = scaler.transform(input_data)
    
    # Make prediction using the selected model
    model = trained_models[model_selection]
    prediction = model.predict(input_scaled)
    
    # Display the prediction
    st.success(f"The predicted closing price is: ${prediction[0]:.2f}")

# Optional: Visualize KNN Hyperparameter Tuning
if st.checkbox("Show KNN Hyperparameter Tuning Plot"):
    k_values = range(1, 31)  # Example range for k
    mse_values = []

    X = df[['Open', 'High', 'Low', 'Volume', 'VWAP']]
    y = df['Close']

    for k in k_values:
        knn_model = KNeighborsRegressor(n_neighbors=k)
        mse = -cross_val_score(knn_model, scaler.transform(X), y, cv=5, scoring='neg_mean_squared_error').mean()
        mse_values.append(mse)

    plt.figure(figsize=(10, 6))
    plt.plot(k_values, mse_values, marker='o', linestyle='-')
    plt.title('KNN Hyperparameter Tuning: MSE vs. Number of Neighbors')
    plt.xlabel('Number of Neighbors (k)')
    plt.ylabel('Mean Squared Error (MSE)')
    plt.xticks(k_values)  # Show all k values on x-axis
    plt.grid()
    
    # Show the plot in Streamlit
    st.pyplot(plt)
