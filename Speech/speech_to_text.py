from pathlib import Path

from Speech.whisper_loader import get_whisper_model

try:
    from Main_UI.config import WHISPER_MODEL
except Exception:
    WHISPER_MODEL = "base"


class SpeechToText:

    def __init__(self):

        self.model = get_whisper_model(WHISPER_MODEL)

    def transcribe(self, audio_path):

        audio_path = Path(audio_path)

        if not audio_path.exists():

            raise FileNotFoundError(
                f"Audio file not found: {audio_path}"
            )

        try:

            result = self.model.transcribe(
                str(audio_path),
                fp16=False
            )

            return {

                "success": True,

                "transcript": result["text"].strip(),

                "language": result.get(
                    "language",
                    "Unknown"
                )

            }

        except Exception as e:

            return {

                "success": False,

                "transcript": "",

                "language": "Unknown",

                "error": str(e)

            }