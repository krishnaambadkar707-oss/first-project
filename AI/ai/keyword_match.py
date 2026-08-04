def keyword_score(user_answer, ideal_answer):

    user = set(
        user_answer.lower().split()
    )

    ideal = set(
        ideal_answer.lower().split()
    )

    common = user.intersection(ideal)

    if len(ideal) == 0:
        return 0

    return (len(common) / len(ideal)) * 100