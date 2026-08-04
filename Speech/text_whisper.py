from Speech.speech_to_text import SpeechToText

stt = SpeechToText()

result = stt.transcribe(

    "uploads/recordings/test.wav"

)

print("\nTranscript")

print("--------------------")

print(result["transcript"])

print()

print("Language :", result["language"])