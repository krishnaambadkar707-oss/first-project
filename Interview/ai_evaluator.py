import os
import json
import google.generativeai as genai


class AIEvaluator:
    """
    Optional LLM-based evaluator (Google Gemini). Requires a
    GEMINI_API_KEY environment variable. Construction raises
    ValueError when no key is configured -- callers should catch
    that and fall back to Interview.evaluator.AnswerEvaluator
    (see Interview/evaluator_factory.py).
    """

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
