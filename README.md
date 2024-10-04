# Stock Price Prediction Project

## Overview

This project focuses on predicting the stock prices of "The State Bank Of India" using machine learning Regression algorithms. The dataset was collected from Yahoo Finance and contains historical stock data.

## Features

- Utilizes various regression algorithms for stock price prediction.
- Dataset collected from Yahoo Finance for "The State Bank Of India."

## Algorithms Used

- Linear Regression
- SVR
- Random Forest
- Gradient Boosting Models (GBM)
- Extreme Gradient Boosting (XGBoost)
- AdaBoostRegressor
- Decision Tree
- KNeighborsRegressor(KNN)
- Artificial Neural Networks (ANN)
- LSTM(Long Short term Memory)

## Dataset

The dataset used in this project is sourced from Yahoo Finance and includes historical stock data for "The State Bank Of India." It comprises relevant features such as Open, High, Low, Close prices, and volume.

## Project Structure

- `data/`: Contains the dataset files.
- `notebooks/`: Jupyter notebooks with the code for data exploration, preprocessing, and model training.
- `src/`: Python source code for the project.
- `requirements.txt`: List of dependencies needed to run the project.

## How to Run

1. Install dependencies using `pip install -r requirements.txt`.
2. Execute the notebooks in the `notebooks/` folder in the given order.
3. Run the scripts in the `src/` folder for further analysis or model training.

## Results

The sequence of all the algorithms used is as follows:
1. Linear Regression
2. SVR
3. Random Forest
4. Gradient Boosting Models (GBM)
5. Extreme Gradient Boosting (XGBoost)
6. AdaBoostRegressor
7. Decision Tree
8. KNeighborsRegressor(KNN)
9. Artificial Neural Networks (ANN)
10. LSTM(Long Short term Memory)

The **Root Mean Square Error (RMSE)** of all the following 10 Regression Algorithms is provided below: 

![image](https://github.com/rohitinu6/Stock-Price-Prediction/assets/113301503/5c3d986f-ef0f-453e-8f5a-e43193489174)

The **Mean Absolute Error (MAE)** of all the following 10 Regression Algorithms is provided below: 

![image](https://github.com/rohitinu6/Stock-Price-Prediction/assets/113301503/50b9a8ae-72c6-4927-8356-18af1f1cacfb)

The **Mean Absolute Percentage Error (MAPE)** of all the following 10 Regression Algorithms is provided below: 

![image](https://github.com/rohitinu6/Stock-Price-Prediction/assets/113301503/4ddab02c-6fa4-414e-b14b-6642dbe6183b)



## Future Work

- We can further combine this data with that of stock sentiment data in order to achieve even better conclusion
- Also we can possibly use Clustering algorithms to develop a buy/sell recommendation system

## Conclusion

- Among the models assessed, AdaBoostRegressor and LSTM emerged as the top performers, showcasing low RMSE, MAE, and MAPE values. These metrics suggest that these algorithms effectively capture the underlying trends and patterns in the stock price data, making them reliable for prediction tasks.
- While some models demonstrated solid predictive capabilities, others, such as Support Vector Regression (SVR) and KNeighborsRegressor, recorded higher RMSE and MAE values. This suggests that these algorithms may produce acceptable predictions on average but are susceptible to significant errors in certain scenarios. Consequently, their reliability in real-world applications could be compromised, highlighting the need for careful consideration when selecting models for stock price predictions.

## Author

Rohit Dubey

## Contributing

We welcome contributions to this project! Please see our [Contributing.md](./CONTRIBUTING.md) file for guidelines on how to get involved.

## License

This project is licensed under the [MIT License](LICENSE).

