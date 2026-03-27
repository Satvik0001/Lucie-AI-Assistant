import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

model = WhisperModel("base", device="cuda", compute_type="float16")

def record_audio(duration=4, samplerate=16000):
    print("Listening...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    return np.squeeze(audio)


def listen_command():
    try:
        audio = record_audio()

        segments, _ = model.transcribe(audio)

        text = " ".join([seg.text for seg in segments]).lower().strip()

        # 🔥 ignore garbage input
        if len(text) < 3:
            return ""

        print("You said:", text)

        return text

    except Exception as e:
        print("Error:", e)
        return ""