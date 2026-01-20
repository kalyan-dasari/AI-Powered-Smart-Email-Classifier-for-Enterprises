import pandas as pd
import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download once
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Text Cleaning Function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"http\S+|www\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]

    return " ".join(words)


# Category Labeling (Rule-based)
def assign_category(text):
    if any(word in text for word in ["offer", "buy", "discount", "click"]):
        return "spam"
    elif any(word in text for word in ["not working", "issue", "problem", "down"]):
        return "complaint"
    elif any(word in text for word in ["request", "refund", "status", "help"]):
        return "request"
    else:
        return "feedback"

# Urgency Labeling
def assign_urgency(text):
    if any(word in text for word in ["asap", "urgent", "immediately", "not working"]):
        return "high"
    elif any(word in text for word in ["refund", "status", "help"]):
        return "medium"
    else:
        return "low"

# Main Pipeline
def main():
    # Read raw CSV safely
    df = pd.read_csv(
        "data/raw_emails.csv",
        encoding="latin1",
        engine="python",
        on_bad_lines="skip"
    )

    # Combine subject + body
    df["combined_text"] = df["subject"].astype(str) + " " + df["body"].astype(str)

    # Clean text
    df["cleaned_text"] = df["combined_text"].apply(clean_text)

    # Assign labels
    df["category"] = df["cleaned_text"].apply(assign_category)
    df["urgency"] = df["cleaned_text"].apply(assign_urgency)

    # Drop temp column
    df.drop(columns=["combined_text"], inplace=True)

    # Save final dataset
    df.to_csv("data/final_emails_dataset.csv", index=False)

    print("✅ Final preprocessed dataset created successfully!")

if __name__ == "__main__":
    main()
