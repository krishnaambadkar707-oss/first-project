class ConfidenceEstimator:

    def __init__(self):

        self.weights = {

            "eye_contact": 0.25,

            "emotion": 0.20,

            "head_pose": 0.15,

            "smile": 0.10,

            "blink": 0.10,

            "face_visibility": 0.10,

            "response_time": 0.10

        }

    def calculate(

        self,

        eye_contact,

        emotion_score,

        head_pose_score,

        smile_score,

        blink_score,

        face_visibility,

        response_time

    ):

        score = (

            eye_contact * self.weights["eye_contact"] +

            emotion_score * self.weights["emotion"] +

            head_pose_score * self.weights["head_pose"] +

            smile_score * self.weights["smile"] +

            blink_score * self.weights["blink"] +

            face_visibility * self.weights["face_visibility"] +

            response_time * self.weights["response_time"]

        )

        return round(score, 2)