import json

import streamlit as st

from resume.upload import upload_resume
from resume.parser import parse_resume
from resume.resume_analyzer import analyze_resume

from Database.database import SessionLocal
from Database.crud import create_resume
from Database.crud import get_resumes_by_user


def show_resume():

    st.title("📄 Resume Analysis")

    st.write(
        "Upload your resume (PDF or DOCX) to get an ATS score and "
        "AI-extracted skills, education, projects, and certifications."
    )

    resume_path = upload_resume()

    if resume_path is None:
        st.info("Please upload your resume to get started.")
        _show_previous_resumes()
        return

    with st.spinner("Analyzing resume..."):
        try:
            resume_text = parse_resume(resume_path)
            report = analyze_resume(resume_text)
        except Exception as exc:
            st.error(f"Could not analyze this resume: {exc}")
            return

    st.session_state.resume_data = report

    # Persist to the database against the logged-in user.
    try:
        db = SessionLocal()
        create_resume(
            db,
            user_id=st.session_state.user_id,
            resume_name=resume_path.rsplit("/", 1)[-1],
            skills=json.dumps(report.get("skills", [])),
            education=json.dumps(report.get("education", [])),
            projects=json.dumps(report.get("projects", [])),
        )
        db.close()
    except Exception as exc:
        st.warning(f"Resume analyzed but could not be saved to history: {exc}")

    st.success("Resume analyzed successfully!")
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATS Score", f"{report.get('ATS Score', 0)}%")

    with col2:
        st.metric("Skills Found", len(report.get("skills", [])))

    with col3:
        st.metric("Projects Found", len(report.get("projects", [])))

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("👤 Personal Information")
        st.write("**Name:**", report.get("name") or "Not Found")
        st.write("**Email:**", report.get("email") or "Not Found")
        st.write("**Phone:**", report.get("phone") or "Not Found")

    with right:
        st.subheader("🎓 Education")
        education = report.get("education", [])
        if education:
            for item in education:
                st.success(item)
        else:
            st.warning("Education not detected.")

    st.divider()
    st.subheader("💻 Skills")

    skills = report.get("skills", [])
    if skills:
        cols = st.columns(4)
        for index, skill in enumerate(skills):
            cols[index % 4].info(skill)
    else:
        st.warning("No skills found.")

    st.divider()
    st.subheader("📂 Projects")

    projects = report.get("projects", [])
    if projects:
        for project in projects:
            st.success(project)
    else:
        st.warning("No projects found.")

    st.divider()
    st.subheader("🏆 Certifications")

    certifications = report.get("certifications", [])
    if certifications:
        for certificate in certifications:
            st.info(certificate)
    else:
        st.warning("No certifications detected.")

    st.divider()
    st.subheader("🧳 Experience")

    experience = report.get("experience", [])
    if experience:
        for item in experience:
            st.info(item)
    else:
        st.warning("No years-of-experience mentions detected.")

    st.divider()
    _show_previous_resumes()


def _show_previous_resumes():

    if "user_id" not in st.session_state:
        return

    try:
        db = SessionLocal()
        resumes = get_resumes_by_user(db, st.session_state.user_id)
        db.close()
    except Exception:
        return

    if not resumes:
        return

    with st.expander(f"Previously uploaded resumes ({len(resumes)})"):
        for r in resumes:
            st.write(
                f"**{r.resume_name}** — uploaded "
                f"{r.uploaded_at.strftime('%d-%m-%Y %H:%M') if r.uploaded_at else ''}"
            )
