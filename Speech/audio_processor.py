import wave
import contextlib


class AudioProcessor:

    def get_duration(self, filepath):

        with contextlib.closing(
            wave.open(filepath, "r")
        ) as file:

            frames = file.getnframes()

            rate = file.getframerate()

            duration = frames / float(rate)

        return round(duration, 2)

    def validate_audio(self, filepath):

        duration = self.get_duration(filepath)

        if duration < 1:

            return False, "Audio is too short."

        if duration > 300:

            return False, "Audio is too long."

        return True, "Audio is valid."