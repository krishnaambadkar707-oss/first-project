from datetime import datetime


class ReportGenerator:

    def __init__(self):

        pass

    # ----------------------------------------
    # Generate Complete Interview Report
    # ----------------------------------------

    def generate(

        self,

        candidate,

        subject,

        difficulty,

        question,

        ideal_answer,

        candidate_answer,

        evaluation,

        timing,

        speech=None,

        confidence=None

    ):

        report = {

            # Candidate Information

            "Candidate": candidate,

            "Date": datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            ),

            "Subject": subject,

            "Difficulty": difficulty,

            # Question

            "Question": question,

            "Ideal Answer": ideal_answer,

            "Candidate Answer": candidate_answer,

            # Evaluation

            "Semantic Score":
                evaluation["semantic"],

            "Keyword Score":
                evaluation["keywords"],

            "Grammar Score":
                evaluation["grammar"],

            "Technical Score":
                evaluation["technical"],

            "Length Score":
                evaluation["length"],

            "Overall Score":
                evaluation["overall"],

            "Feedback":
                evaluation["feedback"],

            # Timing

            "Thinking Time":
                timing["Thinking Time"],

            "Speaking Time":
                timing["Speaking Time"],

            "Response Time":
                timing["Total Response Time"],

            "Words":
                timing["Words"],

            "WPM":
                timing["WPM"],

            "Fluency":
                timing["Fluency"]

        }

        # Speech Module

        if speech:

            report.update(

                {

                    "Transcript":
                        speech["transcript"],

                    "Language":
                        speech["language"]

                }

            )

        # Confidence Module

        if confidence:

            report.update(

                {

                    "Confidence Score":
                        confidence["Confidence"],

                    "Eye Contact":
                        confidence["Eye Contact"],

                    "Blink":
                        confidence["Blink"]

                }

            )

        return report