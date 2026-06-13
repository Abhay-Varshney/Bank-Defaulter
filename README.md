# 💳 Credit Defaulter Prediction System

A Machine Learning-powered web application that predicts whether a customer is likely to default on a loan or credit payment based on financial and personal information.

Built using **Python**, **Streamlit**, **Scikit-Learn**, and a trained classification model.

---

## 🚀 Features

* Predicts whether a customer is a potential credit defaulter.
* User-friendly Streamlit web interface.
* Real-time prediction based on customer details.
* Supports financial, demographic, and repayment history inputs.
* Lightweight and easy to deploy.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* NumPy
* Scikit-Learn
* Pickle

---

## 📂 Project Structure

```text
Credit-Defaulter-Prediction/
│
├── app.py                  # Main Streamlit application
├── model.pkl               # Trained Machine Learning model
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
└── assets/
    └── screenshots/        # Application screenshots (optional)
```

---

## 📊 Input Features

The model uses the following customer information:

| Feature                | Description                       |
| ---------------------- | --------------------------------- |
| Credit Limit Balance   | Available credit limit            |
| Gender                 | Male/Female                       |
| Age                    | Customer age                      |
| Marital Status         | Married/Single/Others             |
| Education              | University / High School / Others |
| Repayment Status (Sep) | Recent repayment status           |
| Repayment Status (Aug) | Previous repayment status         |
| Repayment Status (Jul) | Earlier repayment status          |
| Bill Amount            | Latest bill amount                |
| Payment Amount         | Latest payment amount             |

---

## 🧠 Machine Learning Model

The trained model predicts whether a customer will:

* ✅ **Not Default** → Loan Approved
* ❌ **Default** → Loan Rejected

The model takes customer financial and repayment history as input and returns a binary prediction.

---
