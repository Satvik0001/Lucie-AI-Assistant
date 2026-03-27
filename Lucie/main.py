from voice.listen import listen_command
from voice.speak import speak
from brain.ai import ask_ai

WAKE_WORDS = ["lucie", "lucy", "you see", "lucky"]

def is_wake_word(command):
    return any(word in command for word in WAKE_WORDS)


def main():
    speak("Lucie is online")

    while True:
        command = listen_command()

        if not command:
            continue

        command = command.lower()

        if is_wake_word(command):

            for word in WAKE_WORDS:
                command = command.replace(word, "").strip()

            if not command:
                speak("Yes?")
                command = listen_command()

            # 🔥 REAL AI
            response = ask_ai(command)

            speak(response)


if __name__ == "__main__":
    main()