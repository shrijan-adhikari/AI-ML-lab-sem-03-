# AI/ML Lab Semester 03

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/AI%2FML-Lab-0A84FF?style=for-the-badge" alt="AI/ML Lab" />
</div>

A practical and academic AI/ML repository designed to explore the full workflow of machine learning projects, from raw data exploration to model evaluation and prediction.

## Overview

This lab contains a series of experiments that introduce the key stages of a data science pipeline:

- understanding datasets and feature structure
- cleaning missing and inconsistent values
- performing exploratory data analysis (EDA)
- preparing data for training
- building machine learning models
- evaluating performance and generating predictions

## Experiment Overview

### 1. Experiment 01 — Data Exploration and Basic Insights
This experiment focuses on reading CSV files, understanding dataframe structure, and exploring basic statistics. It introduces important pandas operations such as `df.info()`, `df.describe()`, and column inspection to understand dataset size, types, and numerical distribution.

### 2. Experiment 02 — Missing Value Detection and Data Cleaning
This experiment teaches how to identify null or missing values in a dataset. It emphasizes checking which columns are incomplete, understanding how missing data affects analysis, and applying cleaning strategies such as dropping or imputing missing values.

### 3. Experiment 03 — Exploratory Data Analysis and Preprocessing
This experiment covers the initial analysis and preparation phase of a machine learning workflow. It focuses on visualizing patterns, identifying relationships among variables, and preparing the dataset for modeling through preprocessing steps.

### 4. Experiment 04 — Customer Churn Prediction and Business Insight
This is a practical business-oriented project using the Telco Customer Churn dataset. The goal is to predict whether a customer is likely to churn and analyze patterns behind customer behavior. It combines data cleaning, feature understanding, model training, and business interpretation.

### 5. Experiment 05 — Stock Price Prediction with Linear Regression
This project applies a simple linear regression model to a stock dataset to predict price trends based on historical values. It demonstrates how to split data, train a regression model, evaluate performance, and save the trained model for reuse.

### 6. Experiment 06 — Image Classification with Machine Learning
This experiment introduces image-based machine learning using handwritten digits. It covers data preparation, preprocessing, model training, and evaluation for digit recognition using a classic machine learning approach.

### 7. Experiment 07 — Crop Disease Recognition using CNN
This experiment focuses on image recognition for crop diseases using a convolutional neural network (CNN). It includes data curation, preprocessing, training, evaluation, and deployment of a predictive system for classifying various crop disease categories.

## Repository Structure

| Path | Description |
| --- | --- |
| `experiment-01.ipynb` | Dataset exploration and basic statistical analysis |
| `experiment-02.ipynb` | Missing value analysis and data cleaning |
| `experiment-03.ipynb` | EDA and preprocessing workflow |
| `experiment-04.ipynb` | Customer churn prediction and business intelligence |
| `experiment-05.py` | Stock price prediction using linear regression |
| `experiment-06.ipynb` | Handwritten digit recognition project |
| `experiment-07.ipynb` | CNN-based crop disease recognition |
| `data/` | Datasets used across the experiments |
| `prediction.pickle` | Saved model artifact |
| `.venv/` | Local virtual environment |

## Datasets Included

- `data/telco_data.csv` — telecom customer dataset for churn analysis
- `data/train.csv` — training data for model learning
- `data/test.csv` — testing data for model evaluation
- `data/Predictions.csv` — generated prediction outputs
- `data/stock_data.csv` — stock market data for regression analysis
- `data/car_dataset.data` — car-related dataset used for experimentation
- `data/dataset_1.data` — additional sample data for analysis tasks

## Getting Started

### Prerequisites

- Python 3.10+
- VS Code or any Python IDE
- Jupyter Notebook

### 1) Clone the repository

```bash
git clone https://github.com/shrijan-adhikari/AI-ML-lab-sem-03-.git
cd AI-ML-lab-sem-03-
```

### 2) Create and activate a virtual environment

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Command Prompt:

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

### 3) Install required libraries

```bash
pip install jupyter notebook numpy pandas matplotlib scikit-learn
```

### 4) Launch Jupyter

```bash
jupyter notebook
```

Then open the notebook you want to run and execute the cells in order.

## Recommended Workflow

1. Start with `experiment-01.ipynb` to understand the dataset structure.
2. Move through the missing-data and EDA exercises.
3. Learn the preprocessing steps before training models.
4. Run the prediction and classification notebooks to compare outcomes.
5. Review performance metrics and interpretation of results.

## Learning Outcomes

By the end of this lab, you will have practical experience with:

- data inspection and basic analytics
- null value handling and cleaning strategies
- feature engineering and preprocessing
- model training and evaluation
- classification and regression techniques
- image recognition and CNN concepts
- business-oriented ML interpretation

## Notes

- Keep the `data/` folder intact because the notebooks may reference files using relative paths.
- If any dependency is missing, install it inside the active environment and rerun the notebook.
- This repository is intended for academic learning and practical experimentation.

## Dark Theme Version

A dark-themed version of this README is available here: [README-dark.md](README-dark.md)

## License

This project is intended for educational and learning purposes only.

---

Developed for AI/ML coursework and hands-on experimentation.
