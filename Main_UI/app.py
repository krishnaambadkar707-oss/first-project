import sys
import os

# Make sure the project root (the folder that contains Database/,
# Authentication/, Dashboard/, Interview/, Speech/, Emotion_analysis/,
# resume/, AI/ ...) is importable no matter which directory this app
# is launched from -- e.g. `streamlit run Main_UI/app.py` from the
# project root, or opening this file directly in an IDE.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from dotenv import load_dotenv
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

import streamlit as st
from Database.database import create_tables

# -------------------------
# Authentication
# -------------------------

from Authentication.login import login
from Authentication.register import register
from Authentication.session import (
    check_login,
    logout
)

# -------------------------
# Dashboard Pages
# -------------------------

from Dashboard.home import show_home
from Dashboard.profile import show_profile
from Dashboard.resume import show_resume
from Dashboard.interview import show_interview
from Dashboard.analytics import show_analytics
from Dashboard.report import show_report
from Dashboard.history import show_history
from Dashboard.settings import show_settings


# ---------------------------------------
# Streamlit Configuration
# ---------------------------------------

create_tables()
st.title("AI Interview Bot")

st.set_page_config(

    page_title="AI Powered Interview Bot",

    page_icon="🤖",

    layout="wide",

    initial_sidebar_state="expanded"

)


# ---------------------------------------
# Session
# ---------------------------------------

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


# ---------------------------------------
# Authentication Screen
# ---------------------------------------

if not check_login():

    st.title("🤖 AI Powered Interview Bot")

    option = st.sidebar.radio(

        "Authentication",

        [

            "Login",

            "Register"

        ]

    )

    if option == "Login":

        login()

    else:

        register()

    st.stop()


# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.title("🤖 AI Interview Bot")

st.sidebar.success(

    f"Welcome\n\n{st.session_state.user}"

)

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "👤 Profile",

        "📄 Resume",

        "🎤 Interview",

        "📊 Analytics",

        "📄 Report",

        "🕒 History",

        "⚙️ Settings"

    ]

)


# ---------------------------------------
# Logout
# ---------------------------------------

if st.sidebar.button("🚪 Logout"):

    logout()

    st.rerun()


# ---------------------------------------
# Routing
# ---------------------------------------

if page == "🏠 Home":

    show_home()

elif page == "👤 Profile":

    show_profile()

elif page == "📄 Resume":

    show_resume()

elif page == "🎤 Interview":

    show_interview()

elif page == "📊 Analytics":

    show_analytics()

elif page == "📄 Report":

    show_report()

elif page == "🕒 History":

    show_history()

elif page == "⚙️ Settings":

    show_settings()