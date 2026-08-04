from Interview.interview_engine import InterviewEngine
from Interview.timer import InterviewTimer
from Interview.evaluator import AnswerEvaluator

from Speech.text_to_speech import TextToSpeech
from Speech.speech_to_text import SpeechToText
from Speech.audio_recorder import AudioRecorder


class InterviewController:

    def __init__(self):

        self.engine = InterviewEngine()

        self.timer = InterviewTimer()

        self.tts = TextToSpeech()

        self.recorder = AudioRecorder()

        self.stt = SpeechToText()

        self.evaluator = AnswerEvaluator()

    # ---------------------------------
    # Load Question File
    # ---------------------------------

    def load_questions(self, path):

        self.engine.load(path)

    # ---------------------------------
    # Start Interview
    # ---------------------------------

    def start(

        self,

        subject,

        difficulty,

        total_questions=5

    ):

        self.engine.start(

            subject,

            difficulty,

            total_questions

        )

    # ---------------------------------
    # Next Question
    # ---------------------------------

    def next_question(self):

        question = self.engine.next_question()

        if question is None:

            return None

        self.timer.reset()

        self.timer.start_question()

        return question

    # ---------------------------------
    # Speak Question
    # ---------------------------------

    def speak_question(self, question):

        self.tts.speak(question)

    # ---------------------------------
    # Record Candidate Answer
    # ---------------------------------

    def record_answer(

        self,

        duration=20,

        output_file="recordings/answer.wav"

    ):

        self.timer.start_answer()

        path = self.recorder.record(

            duration,

            output_file

        )

        self.timer.stop_answer()

        result = self.stt.transcribe(path)

        return result

    # ---------------------------------
    # Evaluate Answer
    # ---------------------------------

    def evaluate(

        self,

        transcript,

        ideal_answer

    ):

        evaluation = self.evaluator.evaluate(

            transcript,

            ideal_answer

        )

        self.engine.submit(

            transcript,

            evaluation

        )

        return evaluation

    # ---------------------------------
    # Timer Report
    # ---------------------------------

    def timing_report(

        self,

        transcript

    ):

        return self.timer.report(transcript)

    # ---------------------------------
    # Finish Interview
    # ---------------------------------

    def finish(self):

        return self.engine.report()