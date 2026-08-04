import streamlit as st

from Database.database import SessionLocal
from Database.crud import create_user
from Database.crud import get_user_by_email

from Authentication.auth import hash_password


def register():

    st.subheader("Create Account")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Register"):

        db = SessionLocal()

        if get_user_by_email(db, email):

            st.error("Email already exists.")

            return

        if password != confirm:

            st.error("Passwords do not match.")

            return

        hashed = hash_password(password)

        create_user(
            db,
            name,
            email,
            hashed
        )

        st.success("Registration Successful!")