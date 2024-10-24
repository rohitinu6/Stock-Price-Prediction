<div align="center">

##  📈 Stock Price Prediction 

![Stock Prediction Model](https://raw.githubusercontent.com/alo7lika/Stock-Price-Prediction/refs/heads/main/InvestWise%20-%20Stock%20Prediction%20Model.png)

</div>

<img src="https://raw.githubusercontent.com/alo7lika/Stock-Price-Prediction/refs/heads/main/Images/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

## 📈 GitHub Repository Stats
| 🌟 **Stars** | 🍴 **Forks** | 🐛 **Issues** | 🔔 **Open PRs** | 🔕 **Closed PRs** | 🛠️ **Languages** | ✅ **Contributors** |
|--------------|--------------|---------------|-----------------|------------------|------------------|------------------|
| ![GitHub stars](https://img.shields.io/github/stars/rohitinu6/Stock-Price-Prediction) | ![forks](https://img.shields.io/github/forks/rohitinu6/Stock-Price-Prediction) | ![issues](https://img.shields.io/github/issues/rohitinu6/Stock-Price-Prediction?color=32CD32) | ![pull requests](https://img.shields.io/github/issues-pr/rohitinu6/Stock-Price-Prediction?color=FFFF8F) | ![Closed PRs](https://img.shields.io/github/issues-pr-closed/rohitinu6/Stock-Price-Prediction?color=20B2AA) | ![Languages](https://img.shields.io/github/languages/count/rohitinu6/Stock-Price-Prediction?color=20B2AA) | ![Contributors](https://img.shields.io/github/contributors/rohitinu6/Stock-Price-Prediction?color=00FA9A) |

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

## ✨ Project Structure

Check the project structure here [Project Structure](PROJECT_STRUCTURE.md)

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
![image](images\f23e9194-72de-438d-bd69-744667680d3e.jpeg)

The **Mean Absolute Error (MAE)** of all the following 10 Regression Algorithms is provided below: 

![image](images\085ee2d1-3544-4bed-a558-5b0b801e806b.jpeg)

The **Mean Absolute Percentage Error (MAPE)** of all the following 10 Regression Algorithms is provided below: 

![image](images\6c9ebb5b-a8ed-44de-8842-bf8f5c25990f.jpeg)


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


<div align="center">

| Contributor                                                                                      | Contributor                                                                                      | Contributor                                                                                      | Contributor                                                                                      |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <img src="https://github.com/alo7lika.png" alt="Alolika" width="80"/> <br> <p align="center">[Alolika](https://github.com/alo7lika) 👩‍💻</p> | <img src="https://github.com/smog-root.png" alt="Smog Root" width="80"/> <br> <p align="center">[Smog Root](https://github.com/smog-root) 👨‍💻</p> | <img src="https://github.com/AYUSHI-SHA.png" alt="Ayushi Sha" width="80"/> <br> <p align="center">[Ayushi Sha](https://github.com/AYUSHI-SHA) 👩‍💻</p> | <img src="https://github.com/rohitinu6.png" alt="Rohit Inu" width="80"/> <br> <p align="center">[Rohit Inu](https://github.com/rohitinu6) 👨‍💻</p> |
| <img src="https://github.com/shradiphylleia.png" alt="Shradi Phylleia" width="80"/> <br> <p align="center">[Shradi Phylleia](https://github.com/shradiphylleia) 👩‍💻</p> | <img src="https://github.com/Pankaj4152.png" alt="Pankaj" width="80"/> <br> <p align="center">[Pankaj](https://github.com/Pankaj4152) 👨‍💻</p> | <img src="https://github.com/shristirwt.png" alt="Shristi" width="80"/> <br> <p align="center">[Shristi](https://github.com/shristirwt) 👩‍💻</p> | <img src="https://github.com/features/actions.png" alt="GitHub Actions" width="80"/> <br> <p align="center">[GitHub Actions](https://github.com/features/actions) 👨‍💻</p> |
| <img src="https://github.com/spandana2004.png" alt="Spandana" width="80"/> <br> <p align="center">[Spandana](https://github.com/spandana2004) 👩‍💻</p> | <img src="https://github.com/J-B-Mugundh.png" alt="Mugundh" width="80"/> <br> <p align="center">[Mugundh](https://github.com/J-B-Mugundh) 👨‍💻</p> | <img src="https://github.com/jvedsaqib.png" alt="Saqib" width="80"/> <br> <p align="center">[Saqib](https://github.com/jvedsaqib) 👨‍💻</p> | <img src="https://github.com/balbirs22.png" alt="Balbir Singh" width="80"/> <br> <p align="center">[Balbir Singh](https://github.com/balbirs22) 👨‍💻</p> |
| <img src="https://github.com/RB137.png" alt="RB137" width="80"/> <br> <p align="center">[RB137](https://github.com/RB137) 👨‍💻</p> | <img src="https://github.com/DarshAgrawal14.png" alt="Darsh Agrawal" width="80"/> <br> <p align="center">[Darsh Agrawal](https://github.com/DarshAgrawal14) 👨‍💻</p> | <img src="https://github.com/lkksharma.png" alt="Lokesh Sharma" width="80"/> <br> <p align="center">[Lokesh Sharma](https://github.com/lkksharma) 👨‍💻</p> | <img src="https://github.com/abhishekHegde2000.png" alt="Abhishek Hegde" width="80"/> <br> <p align="center">[Abhishek Hegde](https://github.com/abhishekHegde2000) 👨‍💻</p> |
| <img src="https://github.com/praveenarjun.png" alt="Praveen Arjun" width="80"/> <br> <p align="center">[Praveen Arjun](https://github.com/praveenarjun) 👨‍💻</p> | <img src="https://github.com/KirtiPratihar.png" alt="Kirti Pratihar" width="80"/> <br> <p align="center">[Kirti Pratihar](https://github.com/KirtiPratihar) 👩‍💻</p> | <img src="https://github.com/Maryam0330.png" alt="Maryam" width="80"/> <br> <p align="center">[Maryam](https://github.com/Maryam0330) 👩‍💻</p> | <img src="https://github.com/priyansh985.png" alt="Priyansh" width="80"/> <br> <p align="center">[Priyansh](https://github.com/priyansh985) 👨‍💻</p> |
| <img src="https://github.com/kundana29.png" alt="Kundana" width="80"/> <br> <p align="center">[Kundana](https://github.com/kundana29) 👩‍💻</p> | <img src="https://github.com/SimranShaikh20.png" alt="Simran Shaikh" width="80"/> <br> <p align="center">[Simran Shaikh](https://github.com/SimranShaikh20) 👩‍💻</p> | <img src="https://github.com/sakshamsaraf23.png" alt="Saksham Saraf" width="80"/> <br> <p align="center">[Saksham Saraf](https://github.com/sakshamsaraf23) 👨‍💻</p> | <img src="https://github.com/sapnilmodak.png" alt="Sapnil Modak" width="80"/> <br> <p align="center">[Sapnil Modak](https://github.com/sapnilmodak) 👨‍💻</p> |
| <img src="https://github.com/Dipanita45.png" alt="Dipanita" width="80"/> <br> <p align="center">[Dipanita](https://github.com/Dipanita45) 👩‍💻</p> | <img src="https://github.com/murtaza-sadri-19.png" alt="Murtaza Sadri" width="80"/> <br> <p align="center">[Murtaza Sadri](https://github.com/murtaza-sadri-19) 👨‍💻</p> | <img src="https://github.com/archanasingh11.png" alt="Archana Singh" width="80"/> <br> <p align="center">[Archana Singh](https://github.com/archanasingh11) 👩‍💻</p> |

</div>

### 🎉 Thank You to All Our Amazing Contributors! 🎉

We are incredibly grateful for your dedication and hard work. Your contributions have been invaluable in making this project a success. Thank you for being a part of our journey!

**Let's continue to build great things together! 🚀**


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




