import streamlit as st
from Interview.interviewer import InterviewController
from resume.resume_analyzer import analyze_resume

profile = analyze_resume(text)

st.title("Resume Analysis")

st.metric("ATS Score", profile["ATS Score"])

st.write("### Name")
st.success(profile["name"])

st.write("### Email")
st.info(profile["email"])

st.write("### Phone")
st.info(profile["phone"])

st.write("### Skills")
st.write(profile["skills"])

st.write("### Education")
st.write(profile["education"])

st.write("### Experience")
st.write(profile["experience"])

st.write("### Projects")
st.write(profile["projects"])

st.write("### Certifications")
st.write(profile["certifications"])