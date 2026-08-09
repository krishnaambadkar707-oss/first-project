import streamlit as st

from Interview.interviewer import InterviewController

QUESTION_FILE = "Data/questions.json"


def initialize_session():
    """Initialize Streamlit session state."""

    defaults = {
        "controller": None,
        "interview_started": False,
        "subject": "Python",
        "difficulty": "Easy",
        "total_questions": 5,
        "current_question": None,
        "transcript": "",
        "evaluation": None,
        "interview_report": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def interview_settings():

    st.subheader("⚙ Interview Settings")

    col1, col2 = st.columns(2)

    with col1:
        subject = st.selectbox(
            "Subject",
            [
                "Python",
                "Data Science",
                "Machine Learning",
                "SQL",
                "Artificial Intelligence",
            ],
        )

    with col2:
        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"],
        )

    total_questions = st.slider(
        "Number of Questions", 1, 10, 5
    )

    return subject, difficulty, total_questions


def reset_interview_state():
    for key in (
        "controller",
        "interview_started",
        "current_question",
        "evaluation",
        "transcript",
        "interview_report",
    ):
        if key in st.session_state:
            del st.session_state[key]


def show_start_screen(subject, difficulty, total_questions):

    if st.button("🚀 Start Interview", use_container_width=True):

        controller = InterviewController()
        controller.load_questions(QUESTION_FILE)
        controller.start(subject, difficulty, total_questions)

        st.session_state.controller = controller
        st.session_state.subject = subject
        st.session_state.difficulty = difficulty
        st.session_state.total_questions = total_questions
        st.session_state.interview_started = True
        st.session_state.current_question = controller.next_question()

        if st.session_state.current_question is None:
            st.warning(
                f"No questions available for {subject} / {difficulty}. "
                "Try a different subject or difficulty."
            )
            reset_interview_state()
            return

        st.rerun()


def show_finished_screen(controller):

    st.balloons()
    st.success("🎉 Interview Completed Successfully!")

    report = controller.finish()
    st.session_state.interview_report = report

    st.subheader("📊 Interview Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Questions Attempted", report["Questions Attempted"])
        st.metric("Overall Score", f"{report['Overall Score']}%")

    with col2:
        st.metric("Subject", report["Subject"])
        st.metric("Difficulty", report["Difficulty"])

    with st.expander("Full question-by-question history"):
        st.json(report["History"])

    if st.button("🔄 Start New Interview", use_container_width=True):
        reset_interview_state()
        st.rerun()


def show_question_screen(controller, question):

    current, total = controller.engine.progress()
    st.progress(current / total if total else 0)
    st.caption(f"Question {current} of {total}")

    st.subheader("🧠 Question")
    st.info(question["question"])

    st.divider()
    st.subheader("🎤 Candidate Answer")

    st.session_state.transcript = st.text_area(
        "Type your answer (or record it below)",
        value=st.session_state.transcript,
        height=160,
    )

    col1, col2 = st.columns(2)

    with col1:
        duration = st.slider("Recording Duration (seconds)", 5, 60, 20)

    with col2:
        st.write("")
        if st.button("🎤 Record Answer", use_container_width=True):
            with st.spinner("Recording your answer..."):
                try:
                    speech = controller.record_answer(duration=duration)
                except Exception as exc:
                    speech = {"success": False, "error": str(exc)}

            if speech.get("success"):
                st.session_state.transcript = speech["transcript"]
                st.success("Speech converted successfully.")
                st.rerun()
            else:
                st.error(speech.get("error", "Recording failed."))

    if st.button(
        "🤖 Evaluate Answer", use_container_width=True, type="primary"
    ):
        if not st.session_state.transcript.strip():
            st.warning("Please type or record an answer first.")
        else:
            evaluation = controller.evaluate(
                st.session_state.transcript, question["answer"]
            )
            st.session_state.evaluation = evaluation

    if st.session_state.evaluation:

        result = st.session_state.evaluation

        st.divider()
        st.subheader("📊 Evaluation")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Overall", f"{result['overall']}%")
            st.metric("Semantic", f"{result['semantic']}%")

        with col2:
            st.metric("Keywords", f"{result['keywords']}%")
            st.metric("Grammar", f"{result['grammar']}%")

        with col3:
            st.metric("Technical", f"{result['technical']}%")
            st.metric("Length", f"{result['length']}%")

        st.success(result["feedback"])

        if st.button("➡ Next Question", use_container_width=True):
            st.session_state.transcript = ""
            st.session_state.evaluation = None
            st.session_state.current_question = controller.next_question()
            st.rerun()


def show_interview():

    initialize_session()

    st.title("🎤 AI Interview")
    st.write("Prepare yourself and click **Start Interview**.")

    subject, difficulty, total_questions = interview_settings()
    st.divider()

    if not st.session_state.interview_started:
        show_start_screen(subject, difficulty, total_questions)
        return

    controller = st.session_state.controller
    question = st.session_state.current_question

    if question is None:
        show_finished_screen(controller)
        return

    show_question_screen(controller, question)
