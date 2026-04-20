import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Loan Defaulter Prediction", page_icon="💳")
st.title("💳 Loan Defaulter Prediction")
st.markdown("Fill in the details below to check loan eligibility.")

st.subheader("Personal Details")
col1, col2 = st.columns(2)

with col1:
    limit_bal = st.number_input("Credit Limit Balance", min_value=0.0)
    age = st.number_input("Age", min_value=18, max_value=100)
    sex = st.selectbox("Gender", options=["Male", "Female"])
    marriage = st.selectbox("Marital Status", options=["Married", "Single", "Others"])

with col2:
    education = st.selectbox("Education", ["university", "high_school", "others"])
    pay_0 = st.number_input("Repayment Status (Sep)", min_value=-2, max_value=9)
    pay_2 = st.number_input("Repayment Status (Aug)", min_value=-2, max_value=9)
    pay_3 = st.number_input("Repayment Status (Jul)", min_value=-2, max_value=9)

st.subheader("Financial Details")
col3, col4 = st.columns(2)

with col3:
    bill_amt1 = st.number_input("Bill Amount (Sep)", min_value=0.0)

with col4:
    pay_amt1 = st.number_input("Payment Amount (Sep)", min_value=0.0)

if st.button("🔍 Predict"):
    sex_val = 1 if sex == "Male" else 2
    marriage_val = {"Married": 1, "Single": 2, "Others": 3}[marriage]

    edu_university  = 1 if education == "university"  else 0
    edu_high_school = 1 if education == "high_school" else 0
    edu_others      = 1 if education == "others"      else 0

    input_data = np.array([[
        limit_bal, sex_val, age, pay_0, pay_2, pay_3,
        bill_amt1, pay_amt1, marriage_val,
        edu_high_school, edu_others, edu_university
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❌ You are a Defaulter — Loan Rejected")
    else:
        st.success("✅ You are Not a Defaulter — Loan Approved")