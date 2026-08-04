import re
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_name(text):

    doc = nlp(text)

    for ent in doc.ents:

        if ent.label_ == "PERSON":
            return ent.text

    return "Unknown"


def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""


def extract_phone(text):

    pattern = r"(\+?\d[\d\-\s]{8,15}\d)"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""