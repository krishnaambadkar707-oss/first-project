import whisper

_model = None
_model_name = "base"


def get_whisper_model(model_name=None):
    """
    Lazily load and cache a single Whisper model instance for the
    whole process, so it is only loaded from disk once even though
    SpeechToText() may be constructed more than once per session.
    """

    global _model, _model_name

    if model_name is None:
        model_name = _model_name

    if _model is None or model_name != _model_name:
        _model_name = model_name
        _model = whisper.load_model(model_name)

    return _model
