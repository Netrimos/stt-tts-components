# main_echo.py
from components.audio_io import record_wav
from components.stt import SpeechToText
from components.tts import TextToSpeech

def main():
    wav_path = record_wav("input.wav", seconds=4)
    stt = SpeechToText()
    tts = TextToSpeech(voice="alloy")

    text = stt.transcribe_file(wav_path)
    print("You said:", text)

    tts.speak_local(f"You said: {text}")

if __name__ == "__main__":
    main()

