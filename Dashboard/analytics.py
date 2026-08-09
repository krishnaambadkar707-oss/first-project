import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from Database.database import SessionLocal
from Database.crud import get_interviews_by_user


def show_analytics():

    st.title("Interview Analytics")

    interviews = []

    if "user_id" in st.session_state:
        try:
            db = SessionLocal()
            interviews = get_interviews_by_user(db, st.session_state.user_id)
            db.close()
        except Exception:
            interviews = []

    if not interviews:
        st.info(
            "No interviews yet — analytics will appear here once you've "
            "completed at least one interview."
        )
        return

    latest = interviews[0]

    technical = latest.technical_score or 0
    communication = latest.communication_score or 0
    overall = latest.total_score or 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Latest Overall", f"{overall}%")
    col2.metric("Latest Technical", f"{technical}%")
    col3.metric("Latest Communication", f"{communication}%")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("Score Breakdown (Latest Interview)")

        labels = ["Technical", "Communication"]
        values = [technical, communication]

        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie(values, labels=labels, autopct="%1.1f%%")
        ax.set_title("Latest Interview Breakdown")
        st.pyplot(fig)
        plt.close(fig)

    with right:
        st.subheader("Performance Trend")

        recent = list(reversed(interviews[:10]))
        trend = {f"#{idx+1}": i.total_score or 0 for idx, i in enumerate(recent)}
        st.line_chart(trend)

    st.divider()
    st.subheader("Technical vs Communication (per interview)")

    recent = list(reversed(interviews[:10]))
    comparison = {
        f"#{idx+1}": {
            "Technical": i.technical_score or 0,
            "Communication": i.communication_score or 0,
        }
        for idx, i in enumerate(recent)
    }
    st.bar_chart(
        {
            "Technical": [v["Technical"] for v in comparison.values()],
            "Communication": [v["Communication"] for v in comparison.values()],
        }
    )
