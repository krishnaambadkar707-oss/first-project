import re

PATTERNS = [

    r"B\.?Tech",
    r"Bachelor",
    r"Master",
    r"M\.?Tech",
    r"BE",
    r"Engineering",
    r"Computer Science",
    r"Artificial Intelligence",
    r"Data Science"

]


def extract_education(text):

    education = []

    for pattern in PATTERNS:

        matches = re.findall(pattern, text, re.IGNORECASE)

        education.extend(matches)

    return list(set(education))