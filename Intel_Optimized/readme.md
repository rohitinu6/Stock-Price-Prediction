# Stock Price Prediction - Intel Optimized

Welcome to the Intel Optimized version of the Stock Price Prediction project! This repository leverages the Intel AI Analytics Toolkit, specifically the Intel Distribution of Scikit-Learn and Modin Pandas, to enhance performance and scalability.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to predict stock prices using advanced machine learning techniques optimized for Intel hardware. By utilizing the Intel AI Analytics Toolkit, we achieve faster computations and efficient data handling, making the prediction process more robust and scalable.

## Features

- **Intel Distribution of Scikit-Learn**: Enhanced performance for machine learning algorithms.
- **Modin Pandas**: Accelerated data manipulation and analysis.
- **Optimized Data Preprocessing**: Efficient handling of large datasets.
- **Advanced Prediction Models**: Implementation of ARIMA, SARIMAX, and hybrid models.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/rohitinu6/Stock-Price-Prediction.git
cd Stock-Price-Prediction/Intel_Optimized
pip install -r requirements.txt
```

Ensure you have the Intel AI Analytics Toolkit installed. You can find the installation guide [here](https://software.intel.com/content/www/us/en/develop/tools/oneapi/ai-analytics-toolkit.html).

## Usage

1. **Data Preparation**: Place your stock price data in the `Data` directory.
2. **Run the Models**: Execute the Jupyter notebooks or Python scripts to train and test the models.

Example run the following notebook:
```
jupyter notebook Intel_Optimized/Stock_prediction_Data_Analysis.ipynb
```

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.
```
\Stock-Price-Prediction\Contributing.md
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
\Stock-Price-Prediction\code-of-conduct.md
```

## How Modin Uses Parallel Processing for Fast Computation

Modin leverages parallel processing to speed up data manipulation tasks. By using Ray or Dask as the execution backend, Modin distributes operations across multiple CPU cores, allowing for efficient handling of large datasets. This parallelism ensures that data loading, cleaning, and transformation tasks are performed much faster compared to the traditional pandas library.

### Key Benefits of Modin:

- **Seamless Integration**: Modin's API is designed to be compatible with pandas, so you can switch to Modin with minimal code changes.
- **Scalability**: Efficiently processes large datasets by utilizing all available CPU cores.
- **Performance**: Significant speedup in data manipulation tasks, making it ideal for big data applications.

To use Modin in your project, simply replace the pandas import with Modin:

```python
import modin.pandas as pd
```

This simple change allows you to take advantage of Modin's parallel processing capabilities without modifying your existing pandas code.

## How Intel Scikit-Learn Uses Parallel Processing for Fast Model Training and Evaluation

Intel Scikit-Learn leverages parallel processing to accelerate machine learning tasks. By utilizing Intel's oneAPI Data Analytics Library (oneDAL), it optimizes algorithms to take full advantage of Intel hardware features such as vectorization and multithreading. This results in significant performance improvements for model training, evaluation, and hyperparameter tuning.

### Key Benefits of Intel Scikit-Learn:

- **Speedup**: Faster training and prediction times due to optimized algorithms.
- **Multithreading**: Efficient use of multiple CPU cores to parallelize computations.
- **Vectorization**: Enhanced performance through SIMD (Single Instruction, Multiple Data) operations.
- **Compatibility**: Seamless integration with existing Scikit-Learn code, requiring minimal changes.

To use Intel Scikit-Learn in your project, install the Intel extension for Scikit-Learn:

```bash
pip install scikit-learn-intelex
```

Then, enable the Intel optimizations in your code:

```python
from sklearnex import patch_sklearn
patch_sklearn()
```

This simple setup allows you to benefit from Intel's hardware acceleration, making your machine learning workflows more efficient and scalable.