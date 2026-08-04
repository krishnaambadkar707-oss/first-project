from Interview.question_bank import QuestionBank

class InterviewEngine:

    def __init__(self):

        self.bank = QuestionBank()

        self.subject = None
        self.difficulty = None

        self.total_questions = 0
        self.current_question = 0

        self.score = 0

        self.history = []

        self.current = None

    # ---------------------------------
    # Load Question File
    # ---------------------------------

    def load(self, file_path):

        self.bank.load(file_path)

    # ---------------------------------
    # Start Interview
    # ---------------------------------

    def start(

        self,
        subject,
        difficulty,
        total_questions=5

    ):

        self.subject = subject
        self.difficulty = difficulty

        self.total_questions = total_questions

        self.current_question = 0

        self.score = 0

        self.history.clear()

        self.bank.reset()

    # ---------------------------------
    # Get Next Question
    # ---------------------------------

    def next_question(self):

        if self.current_question >= self.total_questions:

            return None

        question = self.bank.get_question(

            self.subject,

            self.difficulty

        )

        if question is None:

            return None

        self.current_question += 1

        self.current = question

        return question

    # ---------------------------------
    # Save Result
    # ---------------------------------

    def submit(

        self,

        user_answer,

        evaluation

    ):

        if self.current is None:

            return

        self.history.append(

            {

                "Question": self.current["question"],

                "Correct Answer": self.current["answer"],

                "User Answer": user_answer,

                "Evaluation": evaluation

            }

        )

        self.score += evaluation["overall"]

    # ---------------------------------
    # Progress
    # ---------------------------------

    def progress(self):

        return (

            self.current_question,

            self.total_questions

        )

    # ---------------------------------
    # Overall Score
    # ---------------------------------

    def overall_score(self):

        if len(self.history) == 0:

            return 0

        return round(

            self.score /

            len(self.history),

            2

        )

    # ---------------------------------
    # Interview Finished?
    # ---------------------------------

    def finished(self):

        return self.current_question >= self.total_questions

    # ---------------------------------
    # Complete Report
    # ---------------------------------

    def report(self):

        return {

            "Subject": self.subject,

            "Difficulty": self.difficulty,

            "Questions Attempted": len(self.history),

            "Overall Score": self.overall_score(),

            "History": self.history

        }