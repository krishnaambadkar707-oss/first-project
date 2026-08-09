from deepface import DeepFace


class EmotionDetector:

    def __init__(self):

        self.models_loaded = False

    def analyze(self, frame):

        try:

            result = DeepFace.analyze(

                frame,

                actions=["emotion"],

                enforce_detection=False,

                silent=True

            )

            if isinstance(result, list):
                result = result[0]

            emotion = result["dominant_emotion"]

            confidence = result["emotion"][emotion]

            return emotion, confidence

        except Exception:

            return "Unknown", 0
