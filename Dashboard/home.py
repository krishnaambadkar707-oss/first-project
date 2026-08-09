import streamlit as st

from Database.database import SessionLocal
from Database.crud import get_interviews_by_user


def show_home():

    st.title("🤖 AI Interview Bot")

    st.subheader(
        "Welcome to the AI Powered Interview System"
    )

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
            "You haven't completed an interview yet. Head to the "
            "**Interview** page to take your first mock interview — "
            "your scores and progress will show up here afterwards."
        )
        return

    scores = [i.total_score for i in interviews if i.total_score is not None]
    technical = [i.technical_score for i in interviews if i.technical_score is not None]
    communication = [i.communication_score for i in interviews if i.communication_score is not None]

    overall_avg = round(sum(scores) / len(scores), 1) if scores else 0
    technical_avg = round(sum(technical) / len(technical), 1) if technical else 0
    communication_avg = round(sum(communication) / len(communication), 1) if communication else 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Overall Score", f"{overall_avg}%")
    col2.metric("Technical", f"{technical_avg}%")
    col3.metric("Communication", f"{communication_avg}%")
    col4.metric("Interviews Taken", len(interviews))

    st.divider()

    st.write("Recent Performance")

    recent = list(reversed(interviews[:10]))
    chart_data = {
        f"#{idx+1}\n{i.domain}": i.total_score or 0
        for idx, i in enumerate(recent)
    }
    st.bar_chart(chart_data)

    st.caption("Most recent interview: " + interviews[0].domain + " (" + interviews[0].difficulty + ")")
