SKILLS = [

    "Python",
    "Java",
    "C++",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "OpenCV",
    "FastAPI",
    "Flask",
    "Django",
    "Data Science",
    "Power BI",
    "Tableau",
    "Git",
    "Docker",
    "AWS"

]


def extract_skills(text):

    found = []

    lower = text.lower()

    for skill in SKILLS:

        if skill.lower() in lower:

            found.append(skill)

    return list(set(found))