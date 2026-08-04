class BehaviorAnalyzer:

    def analyze(

        self,

        confidence,

        eye_contact,

        emotion,

        smile,

        blink_rate

    ):

        report = {}

        report["Confidence Score"] = confidence

        report["Eye Contact"] = eye_contact

        report["Emotion"] = emotion

        report["Smile"] = smile

        report["Blink Rate"] = blink_rate

        # Overall Assessment
        if confidence >= 90:

            report["Overall"] = "Excellent"

            report["Suggestion"] = (
                "Excellent eye contact, balanced facial "
                "expressions, and consistent engagement."
            )

        elif confidence >= 75:

            report["Overall"] = "Good"

            report["Suggestion"] = (
                "Good overall presentation. Continue "
                "maintaining eye contact and natural expressions."
            )

        elif confidence >= 60:

            report["Overall"] = "Average"

            report["Suggestion"] = (
                "Try maintaining a steadier posture and "
                "look toward the camera more consistently."
            )

        else:

            report["Overall"] = "Needs Improvement"

            report["Suggestion"] = (
                "Practice mock interviews to become more "
                "comfortable speaking on camera."
            )

        return report