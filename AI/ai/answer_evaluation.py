from ai.semantic_similarity import semantic_score
from ai.keyword_match import keyword_score
from ai.grammar_checker import grammar_score
from ai.score_calculator import final_score
from ai.feedback_generator import generate_feedback
from Speech.speech_to_text import SpeechToText
from AI.ai.answer_evaluation import AnswerEvaluator


class AnswerEvaluator:

    def evaluate(
        self,
        user_answer,
        ideal_answer
    ):

        semantic = semantic_score(
            user_answer,
            ideal_answer
        )

        keyword = keyword_score(
            user_answer,
            ideal_answer
        )

        grammar = grammar_score(
            user_answer
        )

        overall = final_score(

            semantic,

            keyword,

            grammar

        )

        feedback = generate_feedback(
            overall
        )

        return {

            "Semantic": round(semantic,2),

            "Keyword": round(keyword,2),

            "Grammar": round(grammar,2),

            "Overall": overall,

            "Feedback": feedback

        }
    
stt = SpeechToText()
evaluator = AnswerEvaluator()

speech = stt.transcribe("uploads/recordings/test.wav")

user_answer = speech["transcript"]

result = evaluator.evaluate(

    user_answer,

    question["answer"]

)

print(result)