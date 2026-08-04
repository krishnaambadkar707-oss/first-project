controller = InterviewController()

controller.load_questions(
    "data/python_questions.json"
)

controller.start(

    subject,

    difficulty,

    total_questions=5

)

question = controller.next_question()

st.write(question["question"])

if st.button("🔊 Read Question"):

    controller.speak_question(

        question["question"]

    )

if st.button("🎤 Record Answer"):

    speech = controller.record_answer()

    transcript = speech["transcript"]

    st.write(transcript)

    result = controller.evaluate(

        transcript,

        question["answer"]

    )

    st.json(result)

    timing = controller.timing_report(

        transcript

    )

    st.json(timing)