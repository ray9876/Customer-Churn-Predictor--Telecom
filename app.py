import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('logistic_model.pkl')

st.title("📊 Customer Churn Prediction")

# Basic Inputs
gender = st.selectbox("Gender", [0, 1])  # You encoded 'Male'/'Female' as 0/1
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", [0, 1])
Dependents = st.selectbox("Dependents", [0, 1])
tenure = st.slider("Tenure", 0, 72, 12)
PhoneService = st.selectbox("Phone Service", [0, 1])
PaperlessBilling = st.selectbox("Paperless Billing", [0, 1])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, value=1000.0)

# One-hot encoded boolean columns (set manually)
InternetService_Fiber_optic = st.selectbox("Internet Service: Fiber optic?", [0, 1])
InternetService_No = st.selectbox("Internet Service: No?", [0, 1])
Contract_One_year = st.selectbox("Contract: One year?", [0, 1])
Contract_Two_year = st.selectbox("Contract: Two year?", [0, 1])
PaymentMethod_Credit_card = st.selectbox("Payment: Credit card?", [0, 1])
PaymentMethod_Electronic_check = st.selectbox("Payment: Electronic check?", [0, 1])
PaymentMethod_Mailed_check = st.selectbox("Payment: Mailed check?", [0, 1])
MultipleLines_No_phone_service = st.selectbox("Multiple Lines: No phone service?", [0, 1])
MultipleLines_Yes = st.selectbox("Multiple Lines: Yes?", [0, 1])
OnlineSecurity_No_internet_service = st.selectbox("Online Security: No internet service?", [0, 1])
OnlineSecurity_Yes = st.selectbox("Online Security: Yes?", [0, 1])
OnlineBackup_No_internet_service = st.selectbox("Online Backup: No internet service?", [0, 1])
OnlineBackup_Yes = st.selectbox("Online Backup: Yes?", [0, 1])
DeviceProtection_No_internet_service = st.selectbox("Device Protection: No internet service?", [0, 1])
DeviceProtection_Yes = st.selectbox("Device Protection: Yes?", [0, 1])
TechSupport_No_internet_service = st.selectbox("Tech Support: No internet service?", [0, 1])
TechSupport_Yes = st.selectbox("Tech Support: Yes?", [0, 1])
StreamingTV_No_internet_service = st.selectbox("Streaming TV: No internet service?", [0, 1])
StreamingTV_Yes = st.selectbox("Streaming TV: Yes?", [0, 1])
StreamingMovies_No_internet_service = st.selectbox("Streaming Movies: No internet service?", [0, 1])
StreamingMovies_Yes = st.selectbox("Streaming Movies: Yes?", [0, 1])



# Feature list (must match the order of features your model was trained on)
features = np.array([[gender, SeniorCitizen, Partner, Dependents, tenure,
                      PhoneService, PaperlessBilling, MonthlyCharges, TotalCharges,
                      InternetService_Fiber_optic, InternetService_No,
                      Contract_One_year, Contract_Two_year,
                      PaymentMethod_Credit_card, PaymentMethod_Electronic_check, PaymentMethod_Mailed_check,
                      MultipleLines_No_phone_service, MultipleLines_Yes,
                      OnlineSecurity_No_internet_service, OnlineSecurity_Yes,
                      OnlineBackup_No_internet_service, OnlineBackup_Yes,
                      DeviceProtection_No_internet_service, DeviceProtection_Yes,
                      TechSupport_No_internet_service, TechSupport_Yes,
                      StreamingTV_No_internet_service, StreamingTV_Yes,
                      StreamingMovies_No_internet_service, StreamingMovies_Yes]])

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(features)[0]
    st.success(f"Churn Prediction: {'Yes' if prediction == 1 else 'No'}")
