document.getElementById('predictForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const cibil_score = document.getElementById('cibil_score').value;
    const loan_amount = document.getElementById('loan_amount').value;

    const response = await fetch('https://loan-approval-prediction-enww.onrender.com/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cibil_score, loan_amount })
    });

    const data = await response.json();
    document.getElementById('result').innerText = data.result === 1 ? '✅ Loan Approved' : '❌ Loan Not Approved';
});