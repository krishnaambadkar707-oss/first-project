def final_score(
    semantic,
    keyword,
    grammar
):

    score = (

        semantic * 0.50 +

        keyword * 0.30 +

        grammar * 0.20

    )

    return round(score,2)