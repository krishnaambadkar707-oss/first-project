import re


class SpeechMetrics:

    def count_words(self, transcript):

        words = re.findall(r"\b[\w'-]+\b", transcript)

        return len(words)

    def speaking_duration(self, duration):

        return round(duration, 2)

    def words_per_minute(self, transcript, duration):

        words = self.count_words(transcript)

        if duration <= 0:

            return 0

        wpm = (words / duration) * 60

        return round(wpm, 2)

    def speaking_rating(self, wpm):

        if wpm < 90:

            return "Slow"

        elif wpm <= 150:

            return "Normal"

        elif wpm <= 180:

            return "Fast"

        else:

            return "Very Fast"

    def pause_estimation(self, duration, transcript):

        words = self.count_words(transcript)

        estimated_speaking_time = words * 0.5

        pause = max(

            0,

            duration - estimated_speaking_time

        )

        return round(pause, 2)

    def fluency_score(self, wpm):

        if 110 <= wpm <= 150:

            return 100

        elif 90 <= wpm <= 170:

            return 85

        elif 70 <= wpm <= 190:

            return 70

        return 50

    def analyze(self, transcript, duration):

        words = self.count_words(transcript)

        wpm = self.words_per_minute(

            transcript,

            duration

        )

        return {

            "Words": words,

            "Duration": duration,

            "WPM": wpm,

            "Rating": self.speaking_rating(wpm),

            "Pause": self.pause_estimation(

                duration,

                transcript

            ),

            "Fluency": self.fluency_score(wpm)

        }