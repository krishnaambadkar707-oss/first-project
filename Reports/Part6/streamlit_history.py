import streamlit as st
import pandas as pd

from database.interview_history import InterviewHistory


def show_history():

    st.title("📈 Interview History")

    history = InterviewHistory()

    rows = history.get_all()

    if not rows:

        st.info("No interview records found.")

        return

    columns = [

        "ID",

        "Candidate",

        "Email",

        "Role",

        "Date",

        "Technical",

        "Communication",

        "Behavior",

        "Resume",

        "Overall",

        "Response Time",

        "WPM",

        "Fluency",

        "Recommendation",

        "Hiring"

    ]

    df = pd.DataFrame(

        rows,

        columns=columns

    )

    st.dataframe(

        df,

        use_container_width=True

    )