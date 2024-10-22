<div align="center">

##  📈 Stock Price Prediction 

![Stock Prediction Model](https://raw.githubusercontent.com/alo7lika/Stock-Price-Prediction/refs/heads/main/InvestWise%20-%20Stock%20Prediction%20Model.png)

</div>

<img src="https://raw.githubusercontent.com/alo7lika/Stock-Price-Prediction/refs/heads/main/Images/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

### This project is now OFFICIALLY accepted for

<div align="center">
  <img src="https://raw.githubusercontent.com/alo7lika/Stock-Price-Prediction/refs/heads/main/Images/329829127-e79eb6de-81b1-4ffb-b6ed-f018bb977e88.png" alt="GSSoC 2024 Extd" width="80%">
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/alo7lika/Stock-Price-Prediction/refs/heads/main/Images/hacktober.png" alt="Hacktober fest 2024" width="80%">
</div>

<br>

<img src="https://raw.githubusercontent.com/alo7lika/Stock-Price-Prediction/refs/heads/main/Images/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

## 📚 Table of Contents

1. [🌟 Overview](#-overview)
2. [🛠️ Features](#️features)
3. [🔍 Algorithms Used](#-algorithms-used)
4. [📊 Dataset](#-dataset)
5. [📁 Project Structure](#-project-structure)
6. [🚀 How to Run](#-how-to-run)
7. [📈 Results](#-results)
8. [📊 Performance Metrics](#-performance-metrics)
9. [🔮 Future Work](#-future-work)
10. [🏆 Conclusion](#-conclusion)
11. [✍️ Author](#-author)
12. [🤝 Contributing](#-contributing)
13. [🌍 Our Valuable Contributors](#-our-valuable-contributors)
14. [📝 License](#-license)

---

## 🌟 Overview

This project focuses on predicting the stock prices of **The State Bank Of India** using machine learning regression algorithms. The dataset was collected from Yahoo Finance and contains historical stock data.

## 🛠️ Features

- Utilizes various regression algorithms for stock price prediction.
- Dataset collected from Yahoo Finance for **The State Bank Of India**.

## 🔍 Algorithms Used

We implemented the following regression algorithms for stock price prediction:

| 🤖 Algorithm                              | 📜 Description                                      |
|-------------------------------------------|----------------------------------------------------|
| Linear Regression                        | A basic regression algorithm.                       |
| Support Vector Regression (SVR)         | Effective for non-linear relationships.             |
| Random Forest                            | Ensemble learning method using decision trees.      |
| Gradient Boosting Models (GBM)          | Sequentially builds models to improve predictions.  |
| Extreme Gradient Boosting (XGBoost)     | Advanced boosting technique with regularization.    |
| AdaBoostRegressor                        | Combines multiple weak learners.                    |
| Decision Tree                            | Simple yet effective model based on tree structure. |
| KNeighborsRegressor (KNN)               | Predicts based on nearest neighbors' average.      |
| Artificial Neural Networks (ANN)        | Mimics human brain for complex data patterns.       |
| Long Short Term Memory (LSTM)           | Suitable for time-series prediction.                |

## 📊 Dataset

The dataset used in this project is sourced from Yahoo Finance and includes historical stock data for **The State Bank Of India**. It comprises relevant features such as:

- 📈 Open prices
- 📉 High prices
- 📉 Low prices
- 💵 Close prices
- 📦 Volume

## 📁 Project Structure

📂 data/ # Contains the dataset files.
📓 notebooks/ # Jupyter notebooks with the code for data exploration, preprocessing, and model training.
🐍 src/ # Python source code for the project.
📋 requirements.txt # List of dependencies needed to run the project.


## 🚀 How to Run

1. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute the notebooks in the `notebooks/` folder in the given order.
3. Run the scripts in the `src/` folder for further analysis or model training.

## 📈 Results

The sequence of all the algorithms used is as follows:

1. Linear Regression
2. SVR
3. Random Forest
4. Gradient Boosting Models (GBM)
5. Extreme Gradient Boosting (XGBoost)
6. AdaBoostRegressor
7. Decision Tree
8. KNeighborsRegressor (KNN)
9. Artificial Neural Networks (ANN)
10. Long Short Term Memory (LSTM)

## 📊 Performance Metrics

The **Root Mean Square Error (RMSE)** of all the following 10 Regression Algorithms is provided below: 

![image](https://github.com/rohitinu6/Stock-Price-Prediction/assets/113301503/5c3d986f-ef0f-453e-8f5a-e43193489174)

The **Mean Absolute Error (MAE)** of all the following 10 Regression Algorithms is provided below: 

![image](https://github.com/rohitinu6/Stock-Price-Prediction/assets/113301503/50b9a8ae-72c6-4927-8356-18af1f1cacfb)

The **Mean Absolute Percentage Error (MAPE)** of all the following 10 Regression Algorithms is provided below: 

![image](https://github.com/rohitinu6/Stock-Price-Prediction/assets/113301503/4ddab02c-6fa4-414e-b14b-6642dbe6183b)


## 🔮 Future Work

- Combine this data with stock sentiment data to enhance prediction accuracy.
- Utilize clustering algorithms to develop a buy/sell recommendation system.

## 🏆 Conclusion

Among the models assessed, **AdaBoostRegressor** and **LSTM** emerged as the top performers, showcasing low RMSE, MAE, and MAPE values. These metrics suggest that these algorithms effectively capture the underlying trends and patterns in the stock price data, making them reliable for prediction tasks.

While some models demonstrated solid predictive capabilities, others, such as **Support Vector Regression (SVR)** and **KNeighborsRegressor**, recorded higher RMSE and MAE values. This indicates that these algorithms may yield acceptable predictions on average but are susceptible to significant errors in certain scenarios, emphasizing the need for careful model selection for stock price predictions.

## ✍️ Author

**Rohit Dubey** 👨‍💻

## 🤝 Contributing

We welcome contributions to this project! Please see our [Contributing.md](./CONTRIBUTING.md) file for guidelines on how to get involved.

## 🌍 Our Valuable Contributors

[![Contributors](https://contrib.rocks/image?repo=rohitinu6/Stock-Price-Prediction)](https://github.com/rohitinu6/Stock-Price-Prediction/graphs/contributors)

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📱 Connect with Us

<div align="center">
  <!-- LinkedIn -->
  <a href="https://www.linkedin.com/in/rohit-dubey-d/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <!-- GitHub -->
  <a href="https://github.com/rohitinu6" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-333333?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <!-- Email -->
  <a href="mailto:rohitinu6@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  <!-- Instagram -->
  <a href="https://www.instagram.com/rohit_dubey_003/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"/>
  </a>
</div>




