def rule_based_urgency(text):
    text = text.lower()

    high_keywords = [
        "urgent", "asap", "immediately", "not working",
        "down", "failure", "critical"
    ]

    medium_keywords = [
        "refund", "reset", "request", "support", "help"
    ]

    for word in high_keywords:
        if word in text:
            return "high"

    for word in medium_keywords:
        if word in text:
            return "medium"

    return None  # fallback to ML
