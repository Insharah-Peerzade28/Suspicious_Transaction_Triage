import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------
st.set_page_config(
    page_title="💳 Suspicious Transaction Triage",
    page_icon="💳",
    layout="wide"
)

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------
st.markdown("""
<style>
.main{
    background-color:#f8f9fa;
}
h1{
    color:#003366;
}
.stButton>button{
    background-color:#003366;
    color:white;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------
st.title("💳 Suspicious Transaction Triage Dashboard")
st.write("### Machine Learning Project for Fraud Detection and Transaction Review Queue")

# -------------------------------------------------------
# LOAD DATASET
# -------------------------------------------------------
@st.cache_data
def load_data():

    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_PATH = BASE_DIR / "data" / "raw" / "credit_card_fraud_10k.csv"

    return pd.read_csv(DATA_PATH)

try:

    df = load_data()
    st.success("✅ Dataset Loaded Successfully")

except Exception as e:

    st.error(f"Dataset not found!\n\n{e}")
    st.stop()

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------
page = st.sidebar.selectbox(

    "Navigation",

    [
        "Dataset Overview",
        "EDA Dashboard",
        "Correlation Heatmap",
        "Raw Dataset",
        "Fraud Prediction"
    ]

)

# =======================================================
# DATASET OVERVIEW
# =======================================================
if page == "Dataset Overview":

    st.header("📊 Dataset Overview")

    col1,col2,col3 = st.columns(3)

    col1.metric("Rows",df.shape[0])
    col2.metric("Columns",df.shape[1])
    col3.metric("Missing Values",df.isnull().sum().sum())

    st.subheader("Column Data Types")

    st.dataframe(df.dtypes.astype(str))

    st.subheader("Statistical Summary")

    st.dataframe(df.describe(include="all"))

# =======================================================
# EDA
# =======================================================
elif page=="EDA Dashboard":

    st.header("📈 Exploratory Data Analysis")

    numeric_columns=df.select_dtypes(include=["int64","float64"]).columns

    feature=st.selectbox(

        "Select Numerical Feature",

        numeric_columns

    )

    col1,col2=st.columns(2)

    with col1:

        fig,ax=plt.subplots(figsize=(6,4))

        sns.histplot(df[feature],bins=30,kde=True,ax=ax)

        ax.set_title(feature)

        st.pyplot(fig)

    with col2:

        fig,ax=plt.subplots(figsize=(6,4))

        sns.boxplot(x=df[feature],ax=ax)

        ax.set_title(feature)

        st.pyplot(fig)

    st.subheader("Fraud Distribution")

    fig,ax=plt.subplots(figsize=(6,4))

    sns.countplot(data=df,x="is_fraud",ax=ax)

    ax.set_xticklabels(["Legitimate","Fraud"])

    st.pyplot(fig)

    st.write(df["is_fraud"].value_counts())

# =======================================================
# CORRELATION
# =======================================================
elif page=="Correlation Heatmap":

    st.header("🔥 Correlation Heatmap")

    corr=df.select_dtypes(include="number").corr()

    fig,ax=plt.subplots(figsize=(10,7))

    sns.heatmap(

        corr,

        annot=True,

        cmap="coolwarm",

        fmt=".2f",

        ax=ax

    )

    st.pyplot(fig)

# =======================================================
# RAW DATA
# =======================================================
elif page=="Raw Dataset":

    st.header("📄 Dataset")

    rows=st.slider(

        "Rows",

        5,

        100,

        10

    )

    st.dataframe(df.head(rows))

    csv=df.to_csv(index=False)

    st.download_button(

        "⬇ Download Dataset",

        csv,

        "credit_card_fraud_10k.csv",

        "text/csv"

    )

# =======================================================
# FRAUD PREDICTION
# =======================================================
elif page=="Fraud Prediction":

    st.header("🤖 Suspicious Transaction Prediction")

    amount=st.number_input("Transaction Amount",0.0)

    transaction_hour=st.slider("Transaction Hour",0,23)

    merchant_category=st.selectbox(

        "Merchant Category",

        sorted(df["merchant_category"].unique())

    )

    foreign_transaction=st.selectbox(

        "Foreign Transaction",

        [0,1]

    )

    location_mismatch=st.selectbox(

        "Location Mismatch",

        [0,1]

    )

    device_trust_score=st.slider(

        "Device Trust Score",

        0.0,

        1.0,

        0.50

    )

    velocity_last_24h=st.slider(

        "Transactions in Last 24 Hours",

        0,

        50,

        5

    )

    cardholder_age=st.slider(

        "Cardholder Age",

        18,

        90,

        30

    )

    if st.button("Predict"):

        score=0

        if amount>500:
            score+=1

        if foreign_transaction==1:
            score+=1

        if location_mismatch==1:
            score+=1

        if device_trust_score<0.4:
            score+=1

        if velocity_last_24h>10:
            score+=1

        if score>=3:

            st.error("🚨 Suspicious Transaction")

            st.write("### Recommendation")

            st.warning("Send this transaction to the fraud investigation queue.")

        else:

            st.success("✅ Legitimate Transaction")

            st.write("### Recommendation")

            st.info("No manual review required.")

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
st.markdown("---")

st.info("""

**A02 – FINTECH**

**Suspicious Transaction Triage**

This dashboard demonstrates exploratory analysis and fraud prediction for educational purposes.

**Limitation:** Predictions should support human analysts and must not replace professional fraud investigations.

""")
