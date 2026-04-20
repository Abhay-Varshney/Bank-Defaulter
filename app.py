from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    for key, value in request.form.items():
        if value == "":
            return render_template('index.html', prediction_text="⚠️ Fill all fields")

    education = request.form['education']

    edu_university = 1 if education == 'university' else 0
    edu_high_school = 1 if education == 'high_school' else 0
    edu_others = 1 if education == 'others' else 0

    input_data = [
        float(request.form['limit_bal']),
        float(request.form['sex']),
        float(request.form['age']),
        float(request.form['pay_0']),
        float(request.form['pay_2']),
        float(request.form['pay_3']),
        float(request.form['bill_amt1']),
        float(request.form['pay_amt1']),
        float(request.form['marriage']),
        edu_high_school,
        edu_others,
        edu_university
    ]

    final_input = np.array([input_data])
    prediction = model.predict(final_input)

    if prediction[0] == 1:
        result = "❌ You are a Defaulter - Loan Rejected"
    else:
        result = "✅ You are Not a Defaulter - Loan Approved"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
