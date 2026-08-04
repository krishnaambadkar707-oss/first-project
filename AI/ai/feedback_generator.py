def generate_feedback(score):

    if score >= 90:

        return (
            "Excellent answer. "
            "Technically strong and well explained."
        )

    elif score >= 75:

        return (
            "Good answer. "
            "Try adding more technical details."
        )

    elif score >= 50:

        return (
            "Average answer. "
            "Needs better explanation."
        )

    else:

        return (
            "Poor answer. "
            "Revise the topic before attempting again."
        )