# whisper_loader.py
import whisper

_model = None

def get_whisper_model(model_name="small"):
    global _model
    if _model is None:
        print("Loading Whisper model...")
        _model = whisper.load_model(model_name)
        print("Model loaded.")
    return _model