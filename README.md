**📧 AI-Powered-Smart-Email-Classifier-for-Enterprises**

**📖 Project Overview**

This project is developed as part of the Springboard Internship Program.
The goal is to build an intelligent system that can automatically classify incoming emails into meaningful categories and detect their urgency level, enabling faster and more efficient handling of enterprise email workflows.

The system uses Natural Language Processing (NLP) and Machine Learning techniques to process raw email data and generate actionable insights.

**🎯 Objectives**

Automate email categorization to reduce manual effort

Detect urgency levels to prioritize critical emails

Build a scalable and enterprise-ready NLP pipeline

Develop reliable baseline ML models for real-world use cases

**🛠️ Tech Stack**

Programming Language: Python

Libraries & Tools:

pandas, numpy

scikit-learn

nltk

Machine Learning Models:

Logistic Regression

Feature Extraction:

TF-IDF Vectorization

Version Control: Git & GitHub

📂 Project Structure

<img width="452" height="736" alt="image" src="https://github.com/user-attachments/assets/899e088f-93d0-42e3-bec0-39005bc23f25" />


**🚀 Milestone Progress**

**✅ Milestone 1: Data Collection & Preprocessing**
Objective: Prepare a clean, labeled dataset for training

Key Work Done:

Collected raw email data in CSV format including sender details and message body

Performed NLP preprocessing:

Removal of URLs, email IDs, punctuation, and noise

Stopword removal

Lemmatization to normalize text

Labeled each email with:

Category: complaint, request, feedback, spam

Urgency: high, medium, low

Handled real-world issues:

Windows CSV encoding problems

Irregular delimiters and noisy enterprise data

Final cleaned dataset stored in CSV format for direct use in training pipelines

📌 **Outcome**: A robust, enterprise-ready labeled dataset suitable for ML model training 

Milestone

**✅ Milestone 2: Email Classification Model**

Objective: Build a baseline email categorization engine

Key Work Done:

Converted cleaned email text into numerical features using TF-IDF

Trained a Logistic Regression multi-class classifier

Evaluated performance using:

Accuracy

Precision

Recall

F1-score

Saved the trained model for future integration

**📊 Results:**

Achieved ~86% accuracy

Established a strong baseline for enterprise email classification

Identified scope for future enhancements using transformer models (BERT / DistilBERT)

**✅ Milestone 3: Urgency Detection Module**

**Objective**: Detect urgency level of incoming emails

Key Work Done:

Developed a hybrid urgency detection system:

Machine Learning model using TF-IDF + Logistic Regression

Rule-based keyword detection for critical cases

Evaluated model using:

Accuracy

F1-score

Confusion Matrix

Improved recall for high-urgency emails using rule-based prioritization

**📊 Results:**

Achieved 88% accuracy

Hybrid approach improved reliability in real-world enterprise scenarios


**✅ Milestone 4: Interactive Dashboard & Deployment**

**Objective**:
Build an interactive user interface for real-time email classification, visualization, and end-to-end usage demonstration.

🔧 Key Work Done
1️⃣ Streamlit-Based Dashboard

Developed a professional UI using Streamlit that enables:

✔ Real-time email simulation (paste subject + body)

✔ Automated category & urgency prediction

✔ Hybrid ML + rule-based classification

✔ Dataset visualization through charts & filters

2️⃣ Data Visualization & Filters

**The dashboard includes:**

📊 Bar Chart – Email count by category

🟣 Pie Chart – Urgency distribution

🔍 Filter Controls – Filter by category & urgency in real-time

📄 Filtered Table View – Displays underlying dataset after filters

This enables users to analyze enterprise email patterns visually.

3️⃣ Real-Time Email Classification UI

Users can submit new emails through the UI:

📝 Input fields for:

Subject

Body

**⚙ System performs:**

Text preprocessing

TF-IDF vectorization

ML classification (category)

Hybrid rule-based urgency detection

The outputs are displayed instantly:

Predicted Category

Predicted Urgency

**4️⃣ Environment & Model Integration**

Integrated saved components from previous milestones:

📂 models/email_category_model.pkl

📂 models/urgency_model.pkl

📂 models/tfidf_vectorizer.pkl

These are loaded at runtime to support:

Fast classification

Low-latency inference

Offline operation

**5️⃣ Deployment Setup**

Prepared and deployed dashboard using:

🚀 Streamlit Community Cloud

Supporting Deployments:

Created requirements.txt

Structured config for Streamlit execution

Shared live production link for evaluation

**📊 Results**

✔ Fully functional interactive dashboard

✔ Successful visualization of dataset insights

✔ Real-time category & urgency classification

✔ Zero manual preprocessing needed at runtime

✔ Cloud accessible via shared deployment URL

**🧩 Tech Used in Milestone 4**

Streamlit for UI & deployment

Matplotlib/Plotly for visualization

Pandas for data filtering

Scikit-Learn for ML inference

Joblib for model loading

**📌 Outcome**

Milestone 4 integrates all previous modules into a user-friendly, deployable system suitable for:

🏢 Enterprise demonstration

📈 Internship evaluation

🧪 Production prototyping

**The system now supports:**

✔ End-to-End data flow

✔ UI-based inference

✔ Interactive analytics

✔ Cloud deployment

**🔗 Live Deployment**

Click below to test the deployed dashboard:

https://ai-powered-smart-email-classifier-for-enterprises-aumixxupzdjd.streamlit.app/

**📜 License**

This project is licensed under the MIT License.

