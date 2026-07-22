# Suspicious Transaction Triage using Machine Learning

## Project Overview

This project was developed for the **A02 – FINTECH: Suspicious Transaction Triage** practical.

Financial institutions process thousands of transactions every day, but fraud analysts can investigate only a small fraction of them. This project develops a machine learning solution to help prioritize suspicious transactions for manual review.

The model predicts whether a transaction should be added to the fraud investigation queue based on transaction characteristics available at decision time.

---

## Problem Statement

Fraud investigations are expensive and time-consuming.

The objective is to identify suspicious transactions while reducing unnecessary investigations.

This is a **binary classification** problem.

Target Variable:

- **0** → Legitimate Transaction
- **1** → Fraudulent Transaction

---

## Objectives

- Perform exploratory data analysis (EDA)
- Clean and preprocess transaction data
- Engineer meaningful features
- Train and compare multiple machine learning models
- Evaluate model performance
- Save the trained model and preprocessing pipeline
- Deploy the model using Streamlit

---

## Dataset

**Dataset Name**

Credit Card Fraud 10K Dataset

**Features**

- transaction_id
- amount
- transaction_hour
- merchant_category
- foreign_transaction
- location_mismatch
- device_trust_score
- velocity_last_24h
- cardholder_age
- is_fraud

Target:

**is_fraud**

---

## Repository Structure

```text
Suspicious_Transaction_Triage/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── data_dictionary.md
│
├── models/
│   ├── fraud_model.pkl
│   ├── pipeline.pkl
│   └── model_metrics.txt
│
├── notebooks/
│   ├── 01_problem_framing.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   └── 06_model_evaluation.ipynb
│
├── reports/
│   ├── figures/
│   └── final_report.pdf
│
├── src/
│   ├── load_data.py
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── tests/
│
├── DATA_CARD.md
├── MODEL_CARD.md
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

---

## Machine Learning Workflow

1. Problem Framing
2. Data Collection
3. Exploratory Data Analysis
4. Data Preprocessing
5. Feature Engineering
6. Model Training
7. Model Evaluation
8. Model Deployment

---

## Models Compared

- Dummy Classifier (Baseline)
- Logistic Regression
- Decision Tree
- Random Forest

(Optional)

- XGBoost

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- PR-AUC

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Suspicious_Transaction_Triage.git
```

Move into the project folder:

```bash
cd Suspicious_Transaction_Triage
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Notebooks

Open the notebooks folder in VS Code or Jupyter Notebook.

Run the notebooks in the following order:

1. 01_problem_framing.ipynb
2. 02_eda.ipynb
3. 03_preprocessing.ipynb
4. 04_feature_engineering.ipynb
5. 05_model_training.ipynb
6. 06_model_evaluation.ipynb

---

## Running the Streamlit App

From the project root:

```bash
streamlit run app/app.py
```

The application will open in your browser.

---

## Expected Outputs

After running the project:

Generated files include:

- processed_transactions.csv
- engineered_transactions.csv
- fraud_model.pkl
- pipeline.pkl
- model_metrics.txt
- figures
- final_report.pdf

---

## Limitations

- Fraud datasets are often highly imbalanced.
- Fraud patterns may change over time.
- The model should support human analysts and not replace manual review.

---

## Future Improvements

- Hyperparameter optimization
- XGBoost and LightGBM comparison
- SHAP explainability
- Real-time fraud detection
- API deployment using FastAPI

---

## Author

Name: **Your Name**

Student ID: **Your Student ID**

Module: **Machine Learning**

Project: **A02 – FINTECH: Suspicious Transaction Triage**

---

## License

This project is developed for academic purposes only.