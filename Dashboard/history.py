import streamlit as st

from Database.database import SessionLocal
from Database.crud import get_interviews_by_user
from Database.crud import get_answers_by_interview


def show_history():

    st.title("Interview History")

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
            "No past interviews yet. Completed interviews will show up "
            "here."
        )
        return

    st.table(
        {
            "Date": [
                i.created_at.strftime("%d %b %Y") if i.created_at else "-"
                for i in interviews
            ],
            "Subject": [i.domain for i in interviews],
            "Difficulty": [i.difficulty for i in interviews],
            "Type": [i.interview_type for i in interviews],
            "Score": [f"{i.total_score}%" if i.total_score is not None else "-" for i in interviews],
        }
    )

    st.divider()
    st.subheader("View a past interview in detail")

    options = {
        f"#{i.id} — {i.domain} ({i.difficulty}) — {i.total_score}% — "
        f"{i.created_at.strftime('%d %b %Y %H:%M') if i.created_at else ''}": i.id
        for i in interviews
    }

    choice = st.selectbox("Select an interview", list(options.keys()))

    if choice:
        interview_id = options[choice]

        try:
            db = SessionLocal()
            answers = get_answers_by_interview(db, interview_id)
            db.close()
        except Exception:
            answers = []

        for idx, a in enumerate(answers, start=1):
            with st.expander(f"Q{idx} — Score: {a.obtained_marks}%"):
                st.write("**Your answer:**", a.user_answer or "_(no answer recorded)_")
                st.write("**Feedback:**", a.feedback or "-")
