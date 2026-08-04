import re


KEYWORDS = [

    "certificate",
    "certification",
    "coursera",
    "udemy",
    "nptel",
    "aws",
    "google"

]


def extract_certifications(text):

    certs = []

    lines = text.split("\n")

    for line in lines:

        for word in KEYWORDS:

            if word.lower() in line.lower():

                certs.append(line)

                break

    return certs