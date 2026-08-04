st.metric(
    "Overall Score",
    f"{overall}%"
)

st.metric(
    "Technical",
    f"{technical}%"
)

st.metric(
    "Communication",
    f"{communication}%"
)

st.metric(
    "Behavior",
    f"{behavior}%"
)

st.metric(
    "Grade",
    calculator.grade(overall)
)