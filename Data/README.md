# ISBM Stock Price Prediction

## Project Overview

This project aims to predict stock prices using RandomForest Regression based on historical stock data of ISBM. The dataset spans from **January 1996 to 2024**, including key stock price attributes such as Open, High, Low, Close, Adjusted Close, and Volume. The model evaluates the performance using various metrics and aims to assist in making data-driven predictions for future stock prices.

### Datasets

The following CSV files are included in the project:

1. **isbm.csv**: This file contains historical stock data for ISBM from 1996 to 2024, including:
   - `Date`: The date of the stock price
   - `Open`: The opening price of the stock
   - `High`: The highest price of the stock during the day
   - `Low`: The lowest price of the stock during the day
   - `Close`: The closing price of the stock at the end of the day
   - `Adj Close`: The adjusted closing price, accounting for dividends and stock splits
   - `Volume`: The total number of shares traded during the day

2. **SBI Train data.csv**: This file contains the training data used to build the stock price prediction model.
3. **SBI Test data.csv**: This file contains the testing data used to evaluate the model's performance.

## Requirements

To run the project, you need the following Python libraries:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

You can install these libraries by running:
```bash
pip install -r requirements.txt
