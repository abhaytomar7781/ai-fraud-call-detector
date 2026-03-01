from keywords import SPAM_KEYWORDS

def analyze_text(text):
    text = text.lower()
    detected = []
    risk_score = 0

    for word, score in SPAM_KEYWORDS.items():
        if word in text:
            detected.append(word)
            risk_score += score

    if risk_score >= 60:
        status = "🚨 FRAUD CALL"
    elif risk_score >= 30:
        status = "⚠️ SUSPICIOUS CALL"
    else:
        status = "✅ SAFE CALL"

    return {
        "detected_keywords": detected,
        "risk_score": risk_score,
        "status": status
    }
