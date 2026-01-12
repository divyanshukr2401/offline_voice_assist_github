from vosk import Model, KaldiRecognizer
import pyaudio

class Listener:
    def __init__(self, model_path):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            rate=16000,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=8192
        )
        self.stream.start_stream()

    def listen(self):                           #converts audio data to json string
        data = self.stream.read(8192, exception_on_overflow=False)
        if self.recognizer.AcceptWaveform(data):
            return self.recognizer.Result()
        return None
