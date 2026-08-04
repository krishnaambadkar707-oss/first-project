# ==========================================
# AI Powered Interview Bot
# app.py
# Part 1 : Main Application
# ==========================================

import streamlit as st
from streamlit_option_menu import option_menu

# ==========================
# Authentication
# ==========================

from Authentication.login import login
from Authentication.register import register
from Authentication.session import (
    check_login,
    logout
)

# ==========================
# Dashboard Pages
# ==========================

from Dashboard.home import show_home
from Dashboard.profile import show_profile
from Dashboard.interview import show_interview
from Dashboard.analytics import show_analytics
from Dashboard.report import show_report
from Dashboard.history import show_history

# ==========================
# Resume Module
# ==========================

from resume.upload import upload_resume
from resume.parser import parse_resume
from resume.resume_analyzer import analyze_resume

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="AI Powered Interview Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# Session State
# ==========================

default_states = {

    "logged_in": False,
    "user": None,

    "question": None,
    "answer": "",

    "report": None,

    "resume_data": None,

    "history": []

}

for key, value in default_states.items():

    if key not in st.session_state:

        st.session_state[key] = value

# ==========================
# Authentication Screen
# ==========================

def authentication():

    st.title("🤖 AI Powered Interview Bot")

    selected = option_menu(

        menu_title=None,

        options=["Login", "Register"],

        icons=["box-arrow-in-right", "person-plus"],

        orientation="horizontal"

    )

    if selected == "Login":

        login()

    else:

        register()

# ==========================
# Sidebar Navigation
# ==========================

def sidebar():

    with st.sidebar:

        st.image(
            "assets/logo.png",
            use_container_width=True
        )

        st.write("---")

        selected = option_menu(

            menu_title="Navigation",

            options=[
                "Home",
                "Resume",
                "Interview",
                "Analytics",
                "Reports",
                "History",
                "Profile"
            ],

            icons=[
                "house",
                "file-earmark-person",
                "camera-video",
                "bar-chart",
                "clipboard-data",
                "clock-history",
                "person-circle"
            ],

            default_index=0

        )

        st.write("---")

        st.success(
            f"👤 {st.session_state.user}"
        )

        if st.button("Logout"):

            logout()

            st.rerun()

    return selected

# ==========================
# Resume Dashboard
# ==========================

def show_resume():

    st.title("📄 Resume Analysis")

    st.write(
        "Upload your resume to get ATS score and AI analysis."
    )

    st.write("")

    resume = upload_resume()

    if resume is None:

        st.info("Please upload your resume.")

        return

    with st.spinner("Analyzing Resume..."):

        resume_text = parse_resume(resume)

        report = analyze_resume(resume_text)

    st.session_state.resume_data = report

    st.success("Resume analyzed successfully!")

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "ATS Score",
            f"{report.get('ATS Score',0)}%"
        )

    with col2:

        st.metric(
            "Skills",
            len(report.get("skills",[]))
        )

    with col3:

        st.metric(
            "Projects",
            len(report.get("projects",[]))
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("👤 Personal Information")

        st.write(
            "**Name:**",
            report.get("name","Not Found")
        )

        st.write(
            "**Email:**",
            report.get("email","Not Found")
        )

        st.write(
            "**Phone:**",
            report.get("phone","Not Found")
        )

    with right:

        st.subheader("🎓 Education")

        education = report.get("education",[])

        if education:

            for item in education:

                st.success(item)

        else:

            st.warning("Education not detected.")

    st.divider()

    st.subheader("💻 Skills")

    skills = report.get("skills",[])

    if skills:

        cols = st.columns(4)

        for index, skill in enumerate(skills):

            cols[index % 4].info(skill)

    else:

        st.warning("No skills found.")

    st.divider()

    st.subheader("📂 Projects")

    projects = report.get("projects",[])

    if projects:

        for project in projects:

            st.success(project)

    else:

        st.warning("No projects found.")

    st.divider()

    st.subheader("🏆 Certifications")

    certifications = report.get("certifications",[])

    if certifications:

        for certificate in certifications:

            st.info(certificate)

    else:

        st.warning("No certifications detected.")

    st.divider()

    st.subheader("⭐ Strengths")

    strengths = report.get("Strengths",[])

    if strengths:

        for strength in strengths:

            st.success(strength)

    else:

        st.warning("No strengths detected.")

# ==========================
# Main Function
# ==========================

def main():

    if not check_login():

        authentication()

        return

    page = sidebar()

    if page == "Home":

        show_home()

    elif page == "Resume":

        show_resume()

    elif page == "Interview":

        show_interview()

    elif page == "Analytics":

        show_analytics()

    elif page == "Reports":

        show_report()

    elif page == "History":

        show_history()

    elif page == "Profile":

        show_profile()


# ==========================
# Run Application
# ==========================

if __name__ == "__main__":

    main()