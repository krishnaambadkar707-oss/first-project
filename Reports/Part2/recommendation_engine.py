class RecommendationEngine:

    def __init__(self):
        pass

    def generate(
        self,
        technical,
        communication,
        behavior,
        resume
    ):

        strengths = []
        improvements = []
        recommendations = []

        # -----------------------------
        # Technical
        # -----------------------------
        if technical >= 85:
            strengths.append("Strong technical knowledge.")
        elif technical >= 70:
            improvements.append("Strengthen advanced technical concepts.")
            recommendations.append(
                "Practice more coding and problem-solving questions."
            )
        else:
            improvements.append("Technical fundamentals need improvement.")
            recommendations.append(
                "Revise core subjects and solve interview questions daily."
            )

        # -----------------------------
        # Communication
        # -----------------------------
        if communication >= 85:
            strengths.append("Excellent communication skills.")
        elif communication >= 70:
            improvements.append("Communication can be improved.")
            recommendations.append(
                "Practice speaking clearly and structuring answers."
            )
        else:
            improvements.append("Communication requires significant improvement.")
            recommendations.append(
                "Participate in mock interviews and public speaking exercises."
            )

        # -----------------------------
        # Behavior
        # -----------------------------
        if behavior >= 85:
            strengths.append("Positive interview behavior.")
        elif behavior >= 70:
            improvements.append("Maintain better eye contact and posture.")
            recommendations.append(
                "Focus on staying engaged throughout the interview."
            )
        else:
            improvements.append("Behavioral presentation needs improvement.")
            recommendations.append(
                "Practice maintaining eye contact and a relaxed posture."
            )

        # -----------------------------
        # Resume
        # -----------------------------
        if resume >= 85:
            strengths.append("Well-structured resume.")
        elif resume >= 70:
            improvements.append("Resume can be improved.")
            recommendations.append(
                "Highlight measurable achievements and projects."
            )
        else:
            improvements.append("Resume requires improvement.")
            recommendations.append(
                "Rewrite the resume using an ATS-friendly format."
            )

        # -----------------------------
        # Hiring Recommendation
        # -----------------------------
        overall = (
            technical * 0.45 +
            communication * 0.25 +
            behavior * 0.20 +
            resume * 0.10
        )

        if overall >= 90:
            hiring = "Highly Recommended"

        elif overall >= 80:
            hiring = "Recommended"

        elif overall >= 70:
            hiring = "Recommended with Improvements"

        else:
            hiring = "Needs More Preparation"

        return {

            "Overall": round(overall, 2),

            "Strengths": strengths,

            "Improvements": improvements,

            "Recommendations": recommendations,

            "Hiring": hiring

        }