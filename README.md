# 📞 AI Fraud Call Detector

An AI-powered web app that detects potential fraud calls by:
- Transcribing audio using OpenAI Whisper
- Analyzing text for suspicious keywords
- Showing fraud risk level in a simple UI

## 🚀 Features
- Upload call recordings (mp3, wav)
- Automatic speech-to-text transcription
- Fraud risk detection using keyword matching
- Clean Streamlit web interface

## 🛠 Tech Stack
- Python
- Streamlit (frontend)
- Whisper (speech-to-text)
- FFmpeg (audio processing)

## ▶ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
