import streamlit as st

from Database.database import SessionLocal
from Database.crud import get_user_by_email

from Authentication.auth import verify_password


def login():

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        db = SessionLocal()

        user = get_user_by_email(db, email)

        if user is None:

            st.error("User not found.")

            return

        if verify_password(
            password,
            user.password
        ):

            st.session_state.logged_in = True
            st.session_state.user = user.full_name
            st.session_state.user_id = user.id

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error("Invalid Password")