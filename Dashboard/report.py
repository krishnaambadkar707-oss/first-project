import streamlit as st


def show_report():

    st.title(

        "Interview Report"

    )

    st.metric(

        "Overall Score",

        "92%"

    )

    st.download_button(

        "Download PDF",

        data=b"",

        file_name="Interview_Report.pdf"

    )