import streamlit as st

from Interview.interviewer import InterviewController


def initialize_session():
    """Initialize Streamlit session state."""

    defaults = {
        "controller": None,
        "interview_started": False,
        "subject": "Python",
        "difficulty": "Easy",
        "total_questions": 5,
        "current_question": None,
        "question_number": 0,
        "report": [],
        "finished": False,
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
                "Artificial Intelligence"
            ]
        )

    with col2:

        difficulty = st.selectbox(
            "Difficulty",
            [
                "Easy",
                "Medium",
                "Hard"
            ]
        )

    total_questions = st.slider(
        "Number of Questions",
        1,
        10,
        5
    )

    return subject, difficulty, total_questions


def show_interview():

    initialize_session()

    st.title("🎤 AI Interview")

    st.write(
        "Prepare yourself and click **Start Interview**."
    )

    subject, difficulty, total_questions = interview_settings()

    st.divider()

    if not st.session_state.interview_started:

        if st.button(
            "🚀 Start Interview",
            use_container_width=True
        ):

            controller = InterviewController()

            controller.load_questions(
                "Data/python_questions.json"
            )

            controller.start(
                subject,
                difficulty,
                total_questions
            )

            st.session_state.controller = controller
            st.session_state.subject = subject
            st.session_state.difficulty = difficulty
            st.session_state.total_questions = total_questions
            st.session_state.interview_started = True

            st.rerun()

        else:

             controller = st.session_state.controller

    # Get first question only once
        if st.session_state.current_question is None:

            question = controller.next_question()

            st.session_state.current_question = question

    question = st.session_state.current_question

    # Interview Finished
    if question is None:

       st.balloons()

       st.success("🎉 Interview Completed Successfully!")

       report = controller.finish()

       st.session_state.interview_report = report

       st.subheader("📊 Interview Summary")

       col1, col2 = st.columns(2)

       with col1:

            st.metric(
                "Questions Attempted",
                report["Questions Attempted"]
            )

            st.metric(
                "Overall Score",
                f"{report['Overall Score']}%"
            )

       with col2:

        st.metric(
            "Subject",
            report["Subject"]
        )

        st.metric(
            "Difficulty",
            report["Difficulty"]
        )

       st.json(report)

       return
   
    st.divider()

st.subheader("🎤 Candidate Answer")

if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "evaluation" not in st.session_state:
    st.session_state.evaluation = None

col1, col2 = st.columns(2)

with col1:

    duration = st.slider(
        "Recording Duration (seconds)",
        5,
        60,
        20
    )

with col2:

    st.write("")
    st.write("")

    if st.button(
        "🎤 Record Answer",
        use_container_width=True
    ):

        with st.spinner("Recording your answer..."):

            speech = controller.record_answer(
                duration=duration
            )

        if speech["success"]:

            st.session_state.transcript = speech["transcript"]

            st.success("Speech converted successfully.")

        else:

            st.error(speech["error"])

st.text_area(

    "Transcript",

    value=st.session_state.transcript,

    height=180

)

if st.button(
    "🔄 Start New Interview",
    use_container_width=True
):

    keys = [

        "controller",

        "interview_started",

        "current_question",

        "evaluation",

        "transcript",

        "speech",

        "interview_report"

    ]

    for key in keys:

        if key in st.session_state:

            del st.session_state[key]

    st.rerun()
        