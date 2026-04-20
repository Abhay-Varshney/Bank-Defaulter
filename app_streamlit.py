import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("💳 Credit Defaulter Prediction")

limit_bal = st.number_input("Credit Limit", min_value=0)
sex = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18)

pay_0 = st.number_input("Repayment Status (Last Month)")
pay_2 = st.number_input("Repayment Status (2 Months Ago)")
pay_3 = st.number_input("Repayment Status (3 Months Ago)")

bill_amt1 = st.number_input("Latest Bill Amount")
pay_amt1 = st.number_input("Last Payment Amount")

marriage = st.selectbox("Marital Status", ["Married", "Single", "Others"])
education = st.selectbox("Education", ["University", "High School", "Others"])

sex_val = 1 if sex == "Male" else 2

marriage_val = 1 if marriage=="Married" else 2 if marriage=="Single" else 3

edu_university = 1 if education == "University" else 0
edu_high_school = 1 if education == "High School" else 0
edu_others = 1 if education == "Others" else 0

# 🔥 Approx normalization (important)
def normalize(x):
    return x / 100000

if st.button("Predict"):
    input_data = np.array([[ 
        normalize(limit_bal),
        sex_val,
        age/100,
        pay_0,
        pay_2,
        pay_3,
        normalize(bill_amt1),
        normalize(pay_amt1),
        marriage_val,
        edu_high_school,
        edu_others,
        edu_university
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❌ You are a Defaulter - Loan Rejected")
    else:
        st.success("✅ You are Not a Defaulter - Loan Approved")
