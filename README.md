# 💳 Loan Approval Prediction Web App

This is a full-stack machine learning web application that predicts loan approval status based on a user's **CIBIL score** and **loan amount**.

🟢 **Live Website**:  
👉 [https://seakty.github.io/Loan-Approval-Prediction/](https://seakty.github.io/Loan-Approval-Prediction/)

🌐 **Backend API (Render)**:  
👉 [https://loan-approval-prediction-enww.onrender.com](https://loan-approval-prediction-enww.onrender.com)

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
## 🌐 Frontend
Open index.html in a browser OR deploy via GitHub Pages.

## 📒 Jupyter Notebook
See the full training process, data cleaning, model accuracy, and feature importance in:

Loan_Prediction_Analysis.ipynb

## 📦 Deployment
🔁 Backend
Hosted on Render:
https://loan-approval-prediction-enww.onrender.com

Flask app binds to 0.0.0.0:$PORT for Render compatibility

## 🌐 Frontend
Deployed via GitHub Pages:
https://seakty.github.io/Loan-Approval-Prediction/

📃 License
MIT License — feel free to reuse or build on top of this for your own projects!
