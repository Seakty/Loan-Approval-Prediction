# 💳 Loan Approval Prediction Web App

This is a full-stack machine learning web application that predicts loan approval status based on a user's **CIBIL score** and **loan amount**.

🟢 **Live Website**:  
👉 [https://seakty.github.io/Loan-Approval-Prediction/](https://seakty.github.io/Loan-Approval-Prediction/)

🌐 **Backend API (Render)**:  
👉 [https://loan-approval-prediction-enww.onrender.com](https://loan-approval-prediction-enww.onrender.com)

---

## 📁 Project Structure

plaintext
Loan-Approval-Prediction/
├── XGBClassifier_model1.pkl       # Trained model file
├── app.py                         # Flask backend (API)
├── requirements.txt               # Python dependencies
├── Loan_Prediction_Analysis.ipynb # Jupyter notebook (training, EDA)
├── index.html                     # Frontend HTML
├── style.css                      # Frontend CSS
├── script.js                      # Frontend JS (fetches prediction)
├── README.md                      # This file
---

## 🧠 How It Works

### 1. Model
- Trained using `XGBoostClassifier` on a dataset with `cibil_score` and `loan_amount` as features
- Target variable is binary: `1` (Approved) or `0` (Not Approved)
- Saved using Python's `pickle`

### 2. Backend
- Built with Flask
- Exposes a `/predict` API endpoint
- Hosted on [Render](https://render.com)

### 3. Frontend
- HTML/CSS/JS form
- Sends input to Flask API and displays prediction result
- Hosted with GitHub Pages

---

## 🛠 Installation (Local Dev)

### 🔗 Backend (Flask API)

```bash
cd backend/
pip install -r requirements.txt
python app.py
```
