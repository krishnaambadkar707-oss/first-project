import streamlit as st


def show_history():

    st.title(

        "Interview History"

    )

    st.table(

        {

            "Date":[

                "15 July",

                "16 July",

                "17 July"

            ],

            "Score":[

                84,

                88,

                92

            ]

        }

    )