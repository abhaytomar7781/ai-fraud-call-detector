import streamlit as st
import whisper
import tempfile
import os

# Page config
st.set_page_config(page_title="AI Fraud Call Detector", layout="centered")

st.title("📞 AI-Powered Fraud Call Detector")
st.write("Upload a call recording and get transcription + fraud risk percentage.")

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

model = load_whisper_model()

uploaded_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    st.success("Audio uploaded successfully!")
    st.audio(uploaded_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_audio_path = tmp_file.name

    with st.spinner("Transcribing audio..."):
        result = model.transcribe(temp_audio_path)

    st.subheader("📝 Transcription")
    text = result["text"]
    st.write(text)

    os.remove(temp_audio_path)

    # 🔥 Weighted fraud keywords
    fraud_keywords = {
        "otp": 4,
        "bank": 3,
        "account": 3,
        "blocked": 2,
        "kyc": 3,
        "urgent": 2,
        "verify": 2,
        "pin": 4,
        "credit card": 4,
        "transfer money": 5,
        "refund": 2
    }

    total_score = 0
    matched_words = []

    text_lower = text.lower()

    for word, weight in fraud_keywords.items():
        if word in text_lower:
            total_score += weight
            matched_words.append(word)

    max_possible_score = sum(fraud_keywords.values())

    fraud_percentage = (total_score / max_possible_score) * 100
    fraud_percentage = min(fraud_percentage, 100)

    st.subheader("🚨 Fraud Risk Analysis")

    # 📊 Show progress bar
    st.progress(int(fraud_percentage))

    # 🎯 Risk level display
    if fraud_percentage > 70:
        st.error(f"🚨 High Risk: {fraud_percentage:.1f}%")
    elif fraud_percentage > 40:
        st.warning(f"⚠️ Moderate Risk: {fraud_percentage:.1f}%")
    else:
        st.success(f"✅ Low Risk: {fraud_percentage:.1f}%")

    if matched_words:
        st.write("🔎 Suspicious keywords detected:")
        st.write(", ".join(matched_words))
    else:
        st.write("No suspicious keywords detected.")
