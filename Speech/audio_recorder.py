import os
import queue
import sounddevice as sd
import soundfile as sf


class AudioRecorder:

    def __init__(self, samplerate=16000, channels=1):

        self.samplerate = samplerate
        self.channels = channels

        self.q = queue.Queue()

    def callback(self, indata, frames, time, status):

        if status:
            print(status)

        self.q.put(indata.copy())

    def record(self, duration, output_path):

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        print(f"Recording for {duration} seconds...")

        with sf.SoundFile(
            output_path,
            mode="w",
            samplerate=self.samplerate,
            channels=self.channels
        ) as file:

            with sd.InputStream(
                samplerate=self.samplerate,
                channels=self.channels,
                callback=self.callback
            ):

                for _ in range(int(duration * self.samplerate / 1024)):
                    file.write(self.q.get())

        print("Recording Completed")

        return output_path