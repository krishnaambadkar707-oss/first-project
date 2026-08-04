import streamlit as st


def show_settings():

    st.title(

        "Settings"

    )

    st.selectbox(

        "Theme",

        [

            "Dark",

            "Light"

        ]

    )

    st.selectbox(

        "Language",

        [

            "English",

            "Hindi"

        ]

    )