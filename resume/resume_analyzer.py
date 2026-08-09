from resume.skill_extractor import extract_skills
from resume.education_extractor import extract_education
from resume.project_extractor import extract_projects
from resume.certification_extractor import extract_certifications
from AI.resume.profile_builder import build_profile
from AI.resume.ats_score import calculate_ats
from AI.resume.experience_extraction import extract_experience


def analyze_resume(text):

    profile = build_profile(text)

    ats_score = calculate_ats(profile=profile)

    return {

        "name": profile.get("name"),

        "email": profile.get("email"),

        "phone": profile.get("phone"),

        "skills":
            extract_skills(text),

        "education":
            extract_education(text),

        "projects":
            extract_projects(text),

        "certifications":
            extract_certifications(text),

        "experience":
            extract_experience(text),

        "profile":
            profile,

        "ATS Score":
            ats_score

    }
