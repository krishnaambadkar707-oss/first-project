from Speech.microphone import MicrophoneRecorder
from Speech.audio_processor import AudioProcessor

recorder = MicrophoneRecorder()

processor = AudioProcessor()

filepath = recorder.record(
    duration=10,
    filename="test.wav"
)

valid, message = processor.validate_audio(filepath)

print("\nValidation :", message)

print("Duration :", processor.get_duration(filepath), "seconds")

print("Saved File :", filepath)