import streamlit as st

from Database.database import SessionLocal
from Database.crud import get_interviews_by_user
from Database.crud import get_answers_by_interview
from Database.crud import get_user_by_id
from Database.crud import get_resumes_by_user

from Reports.Part2.recommendation_engine import RecommendationEngine
from Reports.Part5.pdf_report import PDFReport


def show_report():

    st.title("Interview Report")

    if "user_id" not in st.session_state:
        st.info("Please log in to view your reports.")
        return

    try:
        db = SessionLocal()
        interviews = get_interviews_by_user(db, st.session_state.user_id)
        db.close()
    except Exception as exc:
        st.error(f"Could not load interviews: {exc}")
        return

    if not interviews:
        st.info(
            "No interviews yet — complete an interview to generate a "
            "report."
        )
        return

    options = {
        f"#{i.id} — {i.domain} ({i.difficulty}) — {i.total_score}% — "
        f"{i.created_at.strftime('%d %b %Y %H:%M') if i.created_at else ''}": i.id
        for i in interviews
    }

    choice = st.selectbox("Select an interview", list(options.keys()))
    interview_id = options[choice]
    interview = next(i for i in interviews if i.id == interview_id)

    technical = interview.technical_score or 0
    communication = interview.communication_score or 0
    behavior = interview.confidence_score or 0

    resume_score = 0
    try:
        db = SessionLocal()
        resumes = get_resumes_by_user(db, st.session_state.user_id)
        db.close()
    except Exception:
        resumes = []

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Overall", f"{interview.total_score}%")
    col2.metric("Technical", f"{technical}%")
    col3.metric("Communication", f"{communication}%")
    col4.metric("Subject", interview.domain)

    st.divider()
    st.subheader("Question-by-question Feedback")

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

    st.divider()

    engine = RecommendationEngine()
    rec = engine.generate(
        technical=technical,
        communication=communication,
        behavior=behavior if behavior else 70,
        resume=resume_score if resume_score else 70,
    )

    left, right = st.columns(2)

    with left:
        st.subheader("💪 Strengths")
        for s in rec["Strengths"]:
            st.success(s)
        if not rec["Strengths"]:
            st.write("—")

    with right:
        st.subheader("📈 Areas to Improve")
        for imp in rec["Improvements"]:
            st.warning(imp)
        if not rec["Improvements"]:
            st.write("—")

    st.subheader("🎯 Recommendation")
    st.info(rec["Hiring"])

    st.divider()

    if st.button("📄 Generate PDF Report", use_container_width=True):

        try:
            db = SessionLocal()
            user = get_user_by_id(db, st.session_state.user_id)
            db.close()

            report_data = {
                "name": user.full_name if user else st.session_state.get("user", "Candidate"),
                "email": user.email if user else "-",
                "role": f"{interview.domain} Candidate",
                "date": interview.created_at.strftime("%d %B %Y") if interview.created_at else "-",
                "technical": technical,
                "communication": communication,
                "behavior": behavior if behavior else "N/A",
                "resume": resume_score if resume_score else "N/A",
                "overall": interview.total_score,
                "speech": {"Words": "N/A", "WPM": "N/A", "Fluency": "N/A"},
                "response_time": "N/A",
                "recommendations": rec["Recommendations"] or ["Keep practicing regularly."],
                "hiring": rec["Hiring"],
            }

            pdf_path = PDFReport().generate(report_data)

            with open(pdf_path, "rb") as f:
                pdf_bytes = f.read()

            st.session_state.generated_pdf = pdf_bytes
            st.success("PDF generated!")

        except Exception as exc:
            st.error(f"Could not generate PDF: {exc}")

    if st.session_state.get("generated_pdf"):
        st.download_button(
            "⬇️ Download PDF",
            data=st.session_state.generated_pdf,
            file_name=f"Interview_Report_{interview_id}.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
