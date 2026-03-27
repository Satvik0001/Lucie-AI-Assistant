import subprocess
import tempfile
import os
import uuid
import winsound

PIPER_PATH = r"piper\piper.exe"
MODEL_PATH = r"piper\en_US-lessac-medium.onnx"

def speak(text):
    print("Lucie:", text)

    try:
        filename = f"lucie_{uuid.uuid4().hex}.wav"
        file_path = os.path.join(tempfile.gettempdir(), filename)

        command = f'echo "{text}" | "{PIPER_PATH}" -m "{MODEL_PATH}" -f "{file_path}"'
        subprocess.run(command, shell=True)

        # 🔥 BLOCKING PLAY (no overlap)
        winsound.PlaySound(file_path, winsound.SND_FILENAME)

        # delete after playing
        if os.path.exists(file_path):
            os.remove(file_path)

    except Exception as e:
        print("Audio error:", e)