import whisper

model = whisper.load_model("base")
result = model.transcribe("My intro.m4a")

with open("transcription.txt", "w") as f:
    f.write(result["text"])


from analyzer import analyze_text

with open("transcription.txt", "r") as f:
    text = f.read()

result = analyze_text(text)

print("\n📞 Call Analysis Report")
print("-----------------------")
print("Detected Keywords:", result["detected_keywords"])
print("Risk Score:", result["risk_score"])
print("Status:", result["status"])
