import time


class InterviewTimer:

    def __init__(self):

        self.reset()

    # -----------------------------
    # Reset Timer
    # -----------------------------
    def reset(self):

        self.question_start = None
        self.answer_start = None
        self.answer_end = None

    # -----------------------------
    # Question Displayed
    # -----------------------------
    def start_question(self):

        self.question_start = time.time()

    # -----------------------------
    # User Starts Speaking
    # -----------------------------
    def start_answer(self):

        self.answer_start = time.time()

    # -----------------------------
    # User Finished Speaking
    # -----------------------------
    def stop_answer(self):

        self.answer_end = time.time()

    # -----------------------------
    # Thinking Time
    # -----------------------------
    def thinking_time(self):

        if self.question_start is None or self.answer_start is None:
            return 0

        return round(
            self.answer_start - self.question_start,
            2
        )

    # -----------------------------
    # Speaking Time
    # -----------------------------
    def speaking_time(self):

        if self.answer_start is None or self.answer_end is None:
            return 0

        return round(
            self.answer_end - self.answer_start,
            2
        )

    # -----------------------------
    # Total Response Time
    # -----------------------------
    def total_time(self):

        if self.question_start is None or self.answer_end is None:
            return 0

        return round(
            self.answer_end - self.question_start,
            2
        )

    # -----------------------------
    # Words Per Minute
    # -----------------------------
    def words_per_minute(self, text):

        speaking = self.speaking_time()

        if speaking <= 0:
            return 0

        words = len(text.split())

        return round(
            (words / speaking) * 60,
            2
        )

    # -----------------------------
    # Speaking Speed Rating
    # -----------------------------
    def speed_rating(self, wpm):

        if wpm == 0:
            return "Not Available"

        if wpm < 90:
            return "Too Slow"

        elif wpm < 120:
            return "Slow"

        elif wpm <= 160:
            return "Normal"

        elif wpm <= 190:
            return "Fast"

        return "Too Fast"

    # -----------------------------
    # Fluency Score
    # -----------------------------
    def fluency_score(self, wpm):

        if 120 <= wpm <= 160:
            return 100

        if wpm < 120:
            score = 100 - (120 - wpm)

        else:
            score = 100 - (wpm - 160)

        return max(0, min(100, round(score)))

    # -----------------------------
    # Complete Report
    # -----------------------------
    def report(self, answer):

        wpm = self.words_per_minute(answer)

        return {

            "Thinking Time": self.thinking_time(),

            "Speaking Time": self.speaking_time(),

            "Total Response Time": self.total_time(),

            "Words": len(answer.split()),

            "WPM": wpm,

            "Speed": self.speed_rating(wpm),

            "Fluency": self.fluency_score(wpm)

        }