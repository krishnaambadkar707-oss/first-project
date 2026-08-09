import re

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

try:
    import language_tool_python
except Exception:
    language_tool_python = None


class AnswerEvaluator:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        # language_tool_python needs a local Java runtime and downloads
        # a large grammar-checker server on first use. If Java isn't
        # installed (common on a fresh machine), don't let the whole
        # evaluator -- and therefore the whole interview -- fail to
        # start; just skip grammar scoring instead.
        self.grammar_tool = None

        if language_tool_python is not None:
            try:
                self.grammar_tool = language_tool_python.LanguageTool(
                    "en-US"
                )
            except Exception:
                self.grammar_tool = None

    # ----------------------------------
    # Semantic Similarity
    # ----------------------------------

    def semantic_score(
        self,
        user_answer,
        ideal_answer
    ):

        embeddings = self.model.encode(
            [user_answer, ideal_answer]
        )

        similarity = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )[0][0]

        return round(similarity * 100, 2)

    # ----------------------------------
    # Keyword Matching
    # ----------------------------------

    def keyword_score(
        self,
        user_answer,
        ideal_answer
    ):

        keywords = set(
            re.findall(
                r"\b[a-zA-Z]{3,}\b",
                ideal_answer.lower()
            )
        )

        user_words = set(
            re.findall(
                r"\b[a-zA-Z]{3,}\b",
                user_answer.lower()
            )
        )

        if len(keywords) == 0:
            return 0

        matched = len(
            keywords.intersection(user_words)
        )

        return round(
            matched /
            len(keywords) * 100,
            2
        )

    # ----------------------------------
    # Grammar Score
    # ----------------------------------

    def grammar_score(
        self,
        text
    ):

        if self.grammar_tool is None:
            # Grammar checking unavailable (e.g. no local Java
            # runtime) -- neutral default so overall scoring still
            # works using the other four components.
            return 80

        matches = self.grammar_tool.check(text)

        words = max(
            len(text.split()),
            1
        )

        score = max(
            0,
            100 - len(matches) * 2
        )

        return round(score, 2)

    # ----------------------------------
    # Answer Length
    # ----------------------------------

    def length_score(
        self,
        answer
    ):

        words = len(answer.split())

        if words < 10:
            return 40

        if words < 25:
            return 70

        if words < 50:
            return 90

        return 100

    # ----------------------------------
    # Technical Terms
    # ----------------------------------

    def technical_score(
        self,
        user_answer,
        ideal_answer
    ):

        technical = set(

            word.lower()

            for word in ideal_answer.split()

            if len(word) > 5

        )

        user = set(

            word.lower()

            for word in user_answer.split()

        )

        if len(technical) == 0:

            return 100

        matched = len(
            technical.intersection(user)
        )

        return round(
            matched /
            len(technical) * 100,
            2
        )

    # ----------------------------------
    # AI Feedback
    # ----------------------------------

    def feedback(
        self,
        overall
    ):

        if overall >= 90:

            return (
                "Excellent answer. Strong technical understanding and communication."
            )

        elif overall >= 75:

            return (
                "Good answer. Minor improvements can make it stronger."
            )

        elif overall >= 60:

            return (
                "Average answer. Include more technical details and examples."
            )

        else:

            return (
                "Needs improvement. Focus on core concepts and answer structure."
            )

    # ----------------------------------
    # Complete Evaluation
    # ----------------------------------

    def evaluate(
        self,
        user_answer,
        ideal_answer
    ):

        semantic = self.semantic_score(
            user_answer,
            ideal_answer
        )

        keywords = self.keyword_score(
            user_answer,
            ideal_answer
        )

        grammar = self.grammar_score(
            user_answer
        )

        length = self.length_score(
            user_answer
        )

        technical = self.technical_score(
            user_answer,
            ideal_answer
        )

        overall = round(

            semantic * 0.40 +

            keywords * 0.25 +

            grammar * 0.15 +

            length * 0.10 +

            technical * 0.10,

            2

        )

        return {

            "semantic": semantic,

            "keywords": keywords,

            "grammar": grammar,

            "length": length,

            "technical": technical,

            "overall": overall,

            "feedback": self.feedback(
                overall
            )

        }