import json
import random
from pathlib import Path


class QuestionBank:

    def __init__(self):

        self.questions = []
        self.used_questions = set()

    # -----------------------------
    # Load JSON Question File
    # -----------------------------
    def load(self, file_path):

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"Question file not found: {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as file:
            self.questions = json.load(file)

        self.used_questions.clear()

    # -----------------------------
    # Return Available Subjects
    # -----------------------------
    def get_subjects(self):

        subjects = sorted(
            list(
                {
                    q["subject"]
                    for q in self.questions
                }
            )
        )

        return subjects

    # -----------------------------
    # Return Difficulty Levels
    # -----------------------------
    def get_difficulties(self):

        return [
            "Easy",
            "Medium",
            "Hard"
        ]

    # -----------------------------
    # Reset Used Questions
    # -----------------------------
    def reset(self):

        self.used_questions.clear()

    # -----------------------------
    # Get Random Question
    # -----------------------------
    def get_question(
        self,
        subject,
        difficulty
    ):

        available = [

            q

            for q in self.questions

            if

            q["subject"].lower() == subject.lower()

            and

            q["difficulty"].lower() == difficulty.lower()

            and

            q["question"] not in self.used_questions

        ]

        if len(available) == 0:

            return None

        question = random.choice(available)

        self.used_questions.add(
            question["question"]
        )

        return question

    # -----------------------------
    # Remaining Questions
    # -----------------------------
    def remaining_questions(
        self,
        subject,
        difficulty
    ):

        remaining = [

            q

            for q in self.questions

            if

            q["subject"].lower() == subject.lower()

            and

            q["difficulty"].lower() == difficulty.lower()

            and

            q["question"] not in self.used_questions

        ]

        return len(remaining)