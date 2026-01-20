import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from utils.urgency_rules import rule_based_urgency

# PAGE CONFIG
st.set_page_config(
    page_title="AI Email Intelligence Dashboard",
    layout="wide"
)

st.title("📧 AI Email Intelligence Dashboard")
st.subheader("Enterprise Email Categorization & Urgency Detection")

# LOAD DATA & MODELS
df = pd.read_csv("data/final_emails_dataset.csv", encoding="latin1")

category_model = joblib.load("models/email_category_model.pkl")
category_vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
urgency_model = joblib.load("models/urgency_model.pkl")
urgency_vectorizer = joblib.load("models/urgency_vectorizer.pkl")

# SIDEBAR FILTERS
st.sidebar.header("🔍 Filter Emails")

category_filter = st.sidebar.multiselect(
    "Filter by Category:",
    options=df["category"].unique(),
    default=df["category"].unique()
)

urgency_filter = st.sidebar.multiselect(
    "Filter by Urgency:",
    options=df["urgency"].unique(),
    default=df["urgency"].unique()
)

filtered_df = df[
    (df["category"].isin(category_filter)) &
    (df["urgency"].isin(urgency_filter))
]

# DASHBOARD METRICS
st.write("### 📊 Dashboard Statistics")
c1, c2, c3 = st.columns(3)

c1.metric("Total Emails", len(df))
c2.metric("Filtered Emails", len(filtered_df))
c3.metric("Categories", df["category"].nunique())

# CHARTS WITH FILTERED DATA
st.write("### 📈 Category & Urgency Distribution (Filtered View)")

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.write("📂 Category Distribution")
    cat_counts = filtered_df["category"].value_counts()
    fig1, ax1 = plt.subplots(figsize=(4,4))
    cat_counts.plot(kind="bar", ax=ax1, color="steelblue")
    ax1.set_xlabel("Category")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

with col_chart2:
    st.write("🚨 Urgency Distribution")
    urg_counts = filtered_df["urgency"].value_counts()
    fig2, ax2 = plt.subplots(figsize=(4,4))
    ax2.pie(urg_counts, labels=urg_counts.index, autopct="%1.1f%%", startangle=90)
    ax2.axis("equal")
    st.pyplot(fig2)

# FILTERED DATA TABLE
st.write("### 📁 Filtered Email Records")
st.dataframe(filtered_df.head(15))

# REAL-TIME EMAIL CLASSIFICATION
st.write("---")
st.header("📨 Real-Time Email Classification")

email_subject = st.text_input("Enter Email Subject")
email_body = st.text_area("Enter Email Body")

if st.button("🔍 Classify Email"):
    full_email = email_subject + " " + email_body

    # Category Prediction
    X_cat = category_vectorizer.transform([full_email])
    predicted_category = category_model.predict(X_cat)[0]

    # Urgency Prediction (Hybrid)
    rule_urg = rule_based_urgency(full_email)
    if rule_urg:
        predicted_urgency = rule_urg
    else:
        X_urg = urgency_vectorizer.transform([full_email])
        predicted_urgency = urgency_model.predict(X_urg)[0]

    st.success("🧠 Classification Completed Successfully!")

    # === SHOW ONLY TEXT RESULTS ===
    st.write(f"### 📂 Category: **{predicted_category}**")
    st.write(f"### 🚨 Urgency: **{predicted_urgency}**")
    
# FOOTER
st.write("---")
st.caption("Built using Streamlit & Scikit-learn | Infosys Springboard Internship Project")
