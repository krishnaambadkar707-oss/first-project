import pyttsx3


class TextToSpeech:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 165)
        self.engine.setProperty("volume", 1.0)

        self.voices = self.engine.getProperty("voices")

        if self.voices:
            self.engine.setProperty(
                "voice",
                self.voices[0].id
            )

    def list_voices(self):

        return [

            {
                "index": i,
                "name": voice.name,
                "id": voice.id
            }

            for i, voice in enumerate(self.voices)

        ]

    def change_voice(self, index):

        if 0 <= index < len(self.voices):

            self.engine.setProperty(

                "voice",

                self.voices[index].id

            )

    def set_rate(self, rate):

        self.engine.setProperty(

            "rate",

            max(100, min(rate, 250))

        )

    def set_volume(self, volume):

        self.engine.setProperty(

            "volume",

            max(0.0, min(volume, 1.0))

        )

    def speak(self, text):

        if not text:
            return

        self.engine.say(text)

        self.engine.runAndWait()

    def stop(self):

        self.engine.stop()