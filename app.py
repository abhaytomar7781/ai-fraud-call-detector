import streamlit as st
import whisper
import tempfile
import os

# Page config
st.set_page_config(page_title="AI Fraud Call Detector", layout="centered")

st.title("📞 AI-Powered Fraud Call Detector")
st.write("Upload a call recording and get transcription + fraud risk.")

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

    fraud_keywords = [
        "otp", "bank", "account", "blocked", "kyc",
        "urgent", "verify", "pin", "credit card", "lottery"
    ]

    score = 0
    matched_words = []

    for word in fraud_keywords:
        if word in text.lower():
            score += 1
            matched_words.append(word)

    st.subheader("🚨 Fraud Detection Result")

    if score >= 3:
        st.error("⚠️ High Risk: This call looks like a FRAUD call")
    else:
        st.success("✅ Low Risk: This call seems SAFE")

    st.write("**Matched suspicious words:**", matched_words)
    st.write("**Risk Score:**", score)
