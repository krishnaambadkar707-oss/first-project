import streamlit as st


def show_home():

    st.title("🤖 AI Interview Bot")

    st.subheader(
        "Welcome to the AI Powered Interview System"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Overall Score",
        "92%"
    )

    col2.metric(
        "Technical",
        "94%"
    )

    col3.metric(
        "Communication",
        "90%"
    )

    col4.metric(
        "Behavior",
        "91%"
    )

    st.divider()

    st.write("Recent Performance")

    st.image(
        "assets/charts/radar.png"
    )