import language_tool_python

tool = language_tool_python.LanguageTool(
    "en-US"
)


def grammar_score(answer):

    mistakes = tool.check(answer)

    errors = len(mistakes)

    score = max(
        0,
        100 - (errors * 5)
    )

    return score