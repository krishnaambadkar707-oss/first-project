import os
import json
import google.generativeai as genai
import streamlit as st


class AIEvaluator:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable not found."
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def evaluate(

        self,

        question,

        ideal_answer,

        user_answer

    ):

        prompt = f"""

You are an expert technical interviewer.

Evaluate the candidate.

Question:
{question}

Ideal Answer:
{ideal_answer}

Candidate Answer:
{user_answer}

Return ONLY JSON.

{{
"technical_score":0-100,
"communication_score":0-100,
"completeness_score":0-100,
"confidence_score":0-100,
"overall_score":0-100,
"strengths":[...],
"improvements":[...],
"feedback":"...",
"hiring":"Hire / Maybe / No Hire"
}}

"""

        response = self.model.generate_content(prompt)

        text = response.text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")

        return json.loads(text)
    
    if st.button(
    "🤖 Evaluate Answer",
    use_container_width=True
):

    if not st.session_state.transcript.strip():

        st.warning("Please record your answer first.")

    else:

        result = controller.evaluate(

            st.session_state.transcript,

            question["answer"]

        )

        st.session_state.evaluation = result

    if st.session_state.evaluation:

    result = st.session_state.evaluation

    st.divider()

    st.subheader("📊 AI Evaluation")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Overall",
            f"{result['overall']}%"
        )

        st.metric(
            "Semantic",
            f"{result['semantic']}%"
        )

    with col2:

        st.metric(
            "Keywords",
            f"{result['keywords']}%"
        )

        st.metric(
            "Grammar",
            f"{result['grammar']}%"
        )

    with col3:

        st.metric(
            "Technical",
            f"{result['technical']}%"
        )

        st.metric(
            "Length",
            f"{result['length']}%"
        )

    st.success(result["feedback"])

    st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "➡ Next Question",
        use_container_width=True
    ):

        st.session_state.transcript = ""
        st.session_state.evaluation = None

        next_question = controller.next_question()

        st.session_state.current_question = next_question

        st.rerun()

with col2:

    current, total = controller.engine.progress()

    st.metric(
        "Progress",
        f"{current}/{total}"
    )    