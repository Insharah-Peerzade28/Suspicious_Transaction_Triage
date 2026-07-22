# MODEL CARD

## Project
A02 – FINTECH: Suspicious Transaction Triage

## Model Name
(To be completed)

Example:
Random Forest Classifier

## Model Version
Version 1.0

## Machine Learning Task
Binary Classification

## Objective
Predict whether a financial transaction should be sent to the manual fraud review queue.

## Target Variable
Class

- 0 = Legitimate Transaction
- 1 = Fraudulent Transaction

## Input Features
(To be updated after preprocessing)

Examples:
- Time
- Amount
- V1–V28

## Training Data
Credit Card Fraud 10K Dataset

## Data Split
Training Set: 80%

Testing Set: 20%

Validation:
Cross-validation performed on the training set.

## Preprocessing
- Removed duplicate records
- Handled missing values
- Standardized numerical features
- Prevented data leakage using a preprocessing pipeline

## Algorithms Compared
- Dummy Classifier
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost (optional)

## Selected Model
(To be completed after evaluation)

## Evaluation Metrics
(To be completed)

Example:

- Accuracy:
- Precision:
- Recall:
- F1-score:
- ROC-AUC:
- PR-AUC:

## Strengths
- Fast predictions
- Suitable for fraud detection
- Can prioritize analyst review

## Limitations
- Performance depends on data quality.
- Fraud patterns can change over time (concept drift).
- Requires periodic retraining.

## Ethical Considerations
This model supports human fraud analysts and should not be used as the sole basis for approving or declining transactions.

## Deployment
The trained model is deployed using Streamlit for demonstration purposes.