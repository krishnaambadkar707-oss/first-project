from Interview.interview_engine import InterviewEngine
from Interview.timer import InterviewTimer
from Interview.evaluator import AnswerEvaluator


class InterviewController:
    """
    Text-based scoring (engine/timer/evaluator) is cheap and is set
    up immediately. Voice components (TTS, Whisper STT, the audio
    recorder) are heavy -- they load ML models / open OS audio
    devices -- so they are only imported and constructed the first
    time record_answer()/speak_question() is actually called. This
    means a candidate who only types answers never needs a working
    microphone, speaker, or a downloaded Whisper model.
    """

    def __init__(self):

        self.engine = InterviewEngine()
        self.timer = InterviewTimer()
        self.evaluator = AnswerEvaluator()

        self._tts = None
        self._stt = None
        self._recorder = None

    # ---------------------------------
    # Lazy voice components
    # ---------------------------------

    @property
    def tts(self):
        if self._tts is None:
            from Speech.text_to_speech import TextToSpeech
            self._tts = TextToSpeech()
        return self._tts

    @property
    def stt(self):
        if self._stt is None:
            from Speech.speech_to_text import SpeechToText
            self._stt = SpeechToText()
        return self._stt

    @property
    def recorder(self):
        if self._recorder is None:
            from Speech.audio_recorder import AudioRecorder
            self._recorder = AudioRecorder()
        return self._recorder

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
