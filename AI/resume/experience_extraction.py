import re


def extract_experience(text):

    patterns = [

        r"\d+\+?\s+years",

        r"\d+\s+year",

        r"\d+\s+months"

    ]

    experience = []

    for p in patterns:

        experience.extend(

            re.findall(
                p,
                text,
                re.IGNORECASE
            )
        )

    return experience