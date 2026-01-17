# components/audio_io.py
import sounddevice as sd
import soundfile as sf

def record_wav(path: str, seconds: float = 5.0, samplerate: int = 16000) -> str:
    print("Recording...")
    audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(path, audio, samplerate)
    return path

