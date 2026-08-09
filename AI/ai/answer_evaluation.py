from AI.ai.semantic_similarity import semantic_score
from AI.ai.keyword_match import keyword_score
from AI.ai.grammar_checker import grammar_score
from AI.ai.score_calculator import final_score
from AI.ai.feedback_generator import generate_feedback


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

            "Semantic": round(semantic, 2),

            "Keyword": round(keyword, 2),

            "Grammar": round(grammar, 2),

            "Overall": overall,

            "Feedback": feedback

        }
