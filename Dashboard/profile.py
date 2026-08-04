import streamlit as st


def show_profile():

    st.title("Candidate Profile")

    name = st.text_input("Name")

    email = st.text_input("Email")

    role = st.selectbox(

        "Job Role",

        [

            "AI Engineer",

            "Data Scientist",

            "Python Developer",

            "ML Engineer"

        ]

    )

    experience = st.slider(

        "Experience",

        0,

        10

    )

    if st.button("Save"):

        st.success(
            "Profile Saved Successfully"
        )