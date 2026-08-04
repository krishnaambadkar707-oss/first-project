class ScoreCalculator:

    def __init__(self):

        self.overall_weights = {

            "technical": 0.45,

            "communication": 0.25,

            "behavior": 0.20,

            "resume": 0.10

        }

    # ------------------------------
    # Technical Score
    # ------------------------------
    def technical_score(

        self,

        semantic,

        keywords,

        grammar,

        completeness

    ):

        score = (

            semantic * 0.40 +

            keywords * 0.30 +

            grammar * 0.20 +

            completeness * 0.10

        )

        return round(score, 2)

    # ------------------------------
    # Communication Score
    # ------------------------------
    def communication_score(

        self,

        wpm_score,

        fluency,

        response_time,

        clarity

    ):

        score = (

            wpm_score * 0.30 +

            fluency * 0.30 +

            response_time * 0.20 +

            clarity * 0.20

        )

        return round(score, 2)

    # ------------------------------
    # Behavior Score
    # ------------------------------
    def behavior_score(

        self,

        eye_contact,

        head_pose,

        emotion,

        smile,

        blink,

        face_visibility

    ):

        score = (

            eye_contact * 0.25 +

            head_pose * 0.15 +

            emotion * 0.20 +

            smile * 0.10 +

            blink * 0.10 +

            face_visibility * 0.20

        )

        return round(score, 2)

    # ------------------------------
    # Overall Score
    # ------------------------------
    def overall_score(

        self,

        technical,

        communication,

        behavior,

        resume

    ):

        score = (

            technical * self.overall_weights["technical"] +

            communication * self.overall_weights["communication"] +

            behavior * self.overall_weights["behavior"] +

            resume * self.overall_weights["resume"]

        )

        return round(score, 2)

    # ------------------------------
    # Grade
    # ------------------------------
    def grade(self, score):

        if score >= 90:
            return "A+"

        elif score >= 80:
            return "A"

        elif score >= 70:
            return "B"

        elif score >= 60:
            return "C"

        return "Needs Improvement"