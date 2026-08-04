import whisper
from Speech.speech_to_text import SpeechToText
from Speech.audio_processor import AudioProcessor
from Speech.speech_metrics import SpeechMetrics


class WhisperModel:

    def __init__(self, model_name="small"):

        print("Loading Whisper Model...")

        self.model = whisper.load_model(model_name)

        print("Whisper Model Loaded.")

    def get_model(self):

        return self.model
    
stt = SpeechToText()

processor = AudioProcessor()

metrics = SpeechMetrics()

audio = "uploads/recordings/test.wav"

result = stt.transcribe(audio)

duration = processor.get_duration(audio)

report = metrics.analyze(

    result["transcript"],

    duration

)

print(report)    

