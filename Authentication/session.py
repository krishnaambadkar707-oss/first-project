import streamlit as st


def check_login():

    return st.session_state.get(
        "logged_in",
        False
    )


def logout():

    st.session_state.clear()

    st.rerun()