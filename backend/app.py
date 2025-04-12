from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

model = pickle.load(open('XGBClassifier_model1.pkl', 'rb'))

@app.route('/')
def home():
    return "Loan Approval Predictor Backend is Running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    cibil_score = int(data['cibil_score'])
    loan_amount = int(data['loan_amount'])

    prediction = model.predict(np.array([[cibil_score, loan_amount]]))[0]
    return jsonify({'result': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)