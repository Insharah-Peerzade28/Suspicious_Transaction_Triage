# Data Dictionary

## Project
**A02 – FINTECH: Suspicious Transaction Triage**

## Dataset
Credit Card Fraud 10K Dataset

### Column Descriptions

| Column Name | Data Type | Description |
|--------------|-----------|-------------|
| Time | Numeric | Time elapsed (in seconds) since the first transaction in the dataset. |
| V1 | Float | PCA-transformed feature representing anonymized transaction information. |
| V2 | Float | PCA-transformed feature representing anonymized transaction information. |
| V3 | Float | PCA-transformed feature representing anonymized transaction information. |
| V4 | Float | PCA-transformed feature representing anonymized transaction information. |
| V5 | Float | PCA-transformed feature representing anonymized transaction information. |
| V6 | Float | PCA-transformed feature representing anonymized transaction information. |
| V7 | Float | PCA-transformed feature representing anonymized transaction information. |
| V8 | Float | PCA-transformed feature representing anonymized transaction information. |
| V9 | Float | PCA-transformed feature representing anonymized transaction information. |
| V10 | Float | PCA-transformed feature representing anonymized transaction information. |
| V11 | Float | PCA-transformed feature representing anonymized transaction information. |
| V12 | Float | PCA-transformed feature representing anonymized transaction information. |
| V13 | Float | PCA-transformed feature representing anonymized transaction information. |
| V14 | Float | PCA-transformed feature representing anonymized transaction information. |
| V15 | Float | PCA-transformed feature representing anonymized transaction information. |
| V16 | Float | PCA-transformed feature representing anonymized transaction information. |
| V17 | Float | PCA-transformed feature representing anonymized transaction information. |
| V18 | Float | PCA-transformed feature representing anonymized transaction information. |
| V19 | Float | PCA-transformed feature representing anonymized transaction information. |
| V20 | Float | PCA-transformed feature representing anonymized transaction information. |
| V21 | Float | PCA-transformed feature representing anonymized transaction information. |
| V22 | Float | PCA-transformed feature representing anonymized transaction information. |
| V23 | Float | PCA-transformed feature representing anonymized transaction information. |
| V24 | Float | PCA-transformed feature representing anonymized transaction information. |
| V25 | Float | PCA-transformed feature representing anonymized transaction information. |
| V26 | Float | PCA-transformed feature representing anonymized transaction information. |
| V27 | Float | PCA-transformed feature representing anonymized transaction information. |
| V28 | Float | PCA-transformed feature representing anonymized transaction information. |
| Amount | Float | Monetary value of the transaction. |
| Class | Integer | Target variable. **0 = Legitimate Transaction**, **1 = Fraudulent Transaction**. |

## Target Variable

**Class**

- **0** → Legitimate Transaction
- **1** → Fraudulent Transaction

## Notes

- The features **V1–V28** are anonymized using Principal Component Analysis (PCA) to protect sensitive financial information.
- **Time** and **Amount** are the only non-anonymized numerical features.
- The dataset is intended for binary classification in fraud detection.