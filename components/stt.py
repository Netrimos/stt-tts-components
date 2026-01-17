# components/stt.py
from openai import OpenAI

class SpeechToText:
    def __init__(self, client: OpenAI | None = None, model: str = "gpt-4o-transcribe"):
        self.client = client or OpenAI()
        self.model = model

    def transcribe_file(self, wav_path: str) -> str:
        print("Transcribing...")
        with open(wav_path, "rb") as f:
            transcript = self.client.audio.transcriptions.create(
                file=f,
                model=self.model,
            )
        return transcript.text

