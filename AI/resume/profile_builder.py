from AI.resume.entities import *
from resume.skill_extractor import *
from resume.education_extractor import *
from resume.project_extractor import *
from resume.certification_extractor import *
from AI.resume.experience_extraction import *


def build_profile(text):

    profile = {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "skills": extract_skills(text),

        "education": extract_education(text),

        "experience": extract_experience(text),

        "projects": extract_projects(text),

        "certifications": extract_certifications(text)

    }

    return profile