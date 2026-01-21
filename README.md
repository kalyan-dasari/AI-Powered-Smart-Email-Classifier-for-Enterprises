📧 Intelligent Email Classification & Urgency Detection System
📖 Project Overview

This project is developed as part of the Springboard Internship Program.
The goal is to build an intelligent system that can automatically classify incoming emails into meaningful categories and detect their urgency level, enabling faster and more efficient handling of enterprise email workflows.

The system uses Natural Language Processing (NLP) and Machine Learning techniques to process raw email data and generate actionable insights.

🎯 Objectives

Automate email categorization to reduce manual effort

Detect urgency levels to prioritize critical emails

Build a scalable and enterprise-ready NLP pipeline

Develop reliable baseline ML models for real-world use cases

🛠️ Tech Stack

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
├── data/
│   ├── raw_emails.csv
│   ├── processed_emails.csv
├── training/
│   ├── train_classifier.py
│   ├── train_urgency_model.py
├── models/
│   ├── email_classifier.pkl
│   ├── urgency_model.pkl
├── docs/
│   ├── Kalyan_Agile_Doc
├── README.md
├── LICENSE

🚀 Milestone Progress
✅ Milestone 1: Data Collection & Preprocessing

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

📌 Outcome: A robust, enterprise-ready labeled dataset suitable for ML model training 

Milestone

✅ Milestone 2: Email Classification Model

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

📊 Results:

Achieved ~86% accuracy

Established a strong baseline for enterprise email classification

Identified scope for future enhancements using transformer models (BERT / DistilBERT)

✅ Milestone 3: Urgency Detection Module

Objective: Detect urgency level of incoming emails

Key Work Done:

Developed a hybrid urgency detection system:

Machine Learning model using TF-IDF + Logistic Regression

Rule-based keyword detection for critical cases

Evaluated model using:

Accuracy

F1-score

Confusion Matrix

Improved recall for high-urgency emails using rule-based prioritization

📊 Results:

Achieved 88% accuracy

Hybrid approach improved reliability in real-world enterprise scenarios

📈 Current Status

✔ Data preprocessing pipeline completed
✔ Email classification model trained and evaluated
✔ Urgency detection module implemented
✔ Models saved and ready for integration

🔮 Future Work (Milestone 4)

End-to-end system integration

API or UI-based email ingestion

Model optimization and performance tuning

Real-time email processing

Deployment-ready architecture

📜 License

This project is licensed under the MIT License.
