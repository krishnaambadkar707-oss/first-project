import os
import sounddevice as sd
from scipy.io.wavfile import write


class MicrophoneRecorder:

    def __init__(
        self,
        sample_rate=16000,
        channels=1,
        output_folder="uploads/recordings"
    ):

        self.sample_rate = sample_rate
        self.channels = channels
        self.output_folder = output_folder

        os.makedirs(self.output_folder, exist_ok=True)

    def record(self, duration=10, filename="answer.wav"):

        print(f"\nRecording for {duration} seconds...")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="int16"
        )

        sd.wait()

        filepath = os.path.join(
            self.output_folder,
            filename
        )

        write(filepath, self.sample_rate, audio)

        print("Recording Finished.")

        return filepath