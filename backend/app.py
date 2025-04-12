import os 
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
    port = int(os.environ.get('PORT', 5000))  # 👈 Use Render's PORT if available
    app.run(host='0.0.0.0', port=port, debug=True)  # 👈 BIND TO 0.0.0.0