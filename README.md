# Customer Churn Predictor

A machine learning project built to predict customer churn using the Telco dataset. This app uses Logistic Regression and provides an interactive interface via Streamlit for real-time predictions.

---

## Project Overview

- **Objective:** Predict if a customer is likely to churn based on their service usage and contract details.
- **Model Used:** Logistic Regression
- **Dataset:** Telco Customer Churn (publicly available)
- **Platform:** Streamlit App (deployed using ngrok for demo)

---

## Features

- Full data preprocessing (handling nulls, encoding, scaling)
- Exploratory Data Analysis (EDA) and visualizations
- Model comparison using AUC/ROC (Logistic Regression, Random Forest, XGBoost, etc.)
- Finalized model: **Logistic Regression**
- Real-time prediction app using Streamlit

---

##  Files in this Repo

| File | Description |
|------|-------------|
| `app.py` | Streamlit application for predictions |
| `logistic_model.pkl` | Trained Logistic Regression model |
| `requirements.txt` | List of Python dependencies |
| `README.md` | Project documentation (this file) |

---

##  How to Run Locally

1. Clone the repository or download the ZIP
2. Navigate to the project folder

```bash
pip install -r requirements.txt
streamlit run app.py
