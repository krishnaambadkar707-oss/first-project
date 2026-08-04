from Speech.text_to_speech import TextToSpeech
from Speech.microphone import MicrophoneRecorder
from Speech.speech_to_text import SpeechToText
from Speech.response_time import ResponseTimer
from Speech.speech_metrics import SpeechMetrics

from AI.ai.answer_evaluation import AnswerEvaluator


class VoiceInterview:

    def __init__(self):

        self.tts = TextToSpeech()

        self.recorder = MicrophoneRecorder()

        self.stt = SpeechToText()

        self.timer = ResponseTimer()

        self.metrics = SpeechMetrics()

        self.evaluator = AnswerEvaluator()

    def conduct_interview(

        self,

        question,

        ideal_answer

    ):

        print("=" * 60)

        print("AI INTERVIEW BOT")

        print("=" * 60)

        print("\nQuestion :")

        print(question)

        self.tts.speak(question)

        # Start Response Timer
        self.timer.start()

        # Record Candidate
        audio_path = self.recorder.record(
            duration=30,
            filename="answer.wav"
        )

        # Stop Timer
        self.timer.stop()

        response_time = self.timer.response_time()

        # Speech To Text
        speech = self.stt.transcribe(audio_path)

        transcript = speech["transcript"]

        # Speech Metrics
        duration = self.metrics.speaking_duration(30)

        speech_report = self.metrics.analyze(
            transcript,
            duration
        )

        # AI Evaluation
        evaluation = self.evaluator.evaluate(
            transcript,
            ideal_answer
        )

        return {

            "Question": question,

            "Transcript": transcript,

            "Response Time": response_time,

            "Speech": speech_report,

            "Evaluation": evaluation

        }