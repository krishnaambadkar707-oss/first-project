from resume.skill_extractor import extract_skills
from resume.education_extractor import extract_education
from resume.project_extractor import extract_projects
from resume.certification_extractor import extract_certifications
from AI.resume.profile_builder import build_profile
from AI.resume.ats_score import calculate_ats


def analyze_resume(text):

    return {

        "skills":
            extract_skills(text),

        "education":
            extract_education(text),

        "projects":
            extract_projects(text),

        "certifications":
            extract_certifications(text),

        "profile":
            build_profile(text), 
            
        "ATS score":
            calculate_ats(profile=build_profile(text))         

    }