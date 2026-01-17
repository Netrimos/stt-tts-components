# components/tts.py
from openai import OpenAI
import io
import wave
import numpy as np
import sounddevice as sd

class TextToSpeech:
    def __init__(
        self,
        client: OpenAI | None = None,
        model: str = "gpt-4o-mini-tts",
        voice: str = "alloy",
    ):
        self.client = client or OpenAI()
        self.model = model
        self.voice = voice

    def speak_local(self, text: str) -> None:
        print("Requesting speech...")
        resp = self.client.audio.speech.create(
            model=self.model,
            voice=self.voice,
            input=text,
            response_format="wav",
        )

        wav_bytes = io.BytesIO(resp.read())
        with wave.open(wav_bytes, "rb") as wf:
            samplerate = wf.getframerate()
            channels = wf.getnchannels()
            sampwidth = wf.getsampwidth()
            frames = wf.readframes(wf.getnframes())

        dtype_map = {1: np.int8, 2: np.int16, 4: np.int32}
        audio = np.frombuffer(frames, dtype=dtype_map[sampwidth])

        if channels > 1:
            audio = audio.reshape(-1, channels)

        print("Playing audio...")
        sd.play(audio, samplerate)
        sd.wait()

