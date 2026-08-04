import pdfplumber
from docx import Document


def extract_pdf(path):

    text = ""

    with pdfplumber.open(path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_docx(path):

    doc = Document(path)

    text = ""

    for para in doc.paragraphs:

        text += para.text + "\n"

    return text


def parse_resume(path):

    if path.endswith(".pdf"):

        return extract_pdf(path)

    elif path.endswith(".docx"):

        return extract_docx(path)

    return ""