# Lucie AI Assistant 🤖

Lucie is a voice-controlled AI assistant built using Python, Whisper (GPU), and local LLM integration.

## 🚀 Features

* 🎤 Speech-to-text using Whisper (GPU accelerated)
* 🧠 AI responses using local LLM (Ollama / Llama3)
* 🎙️ Text-to-speech using Piper
* ⚙️ Modular architecture (voice, brain, control)

## 🛠️ Tech Stack

* Python
* faster-whisper
* Piper TTS
* Ollama (Llama3)
* 
## 🔊 Voice Setup (Piper)

This project uses Piper for text-to-speech.

Due to file size, Piper models are not included in this repository.

### Setup Instructions:

1. Download Piper from: https://github.com/rhasspy/piper
2. Place the `piper` folder inside the project directory
3. Add your voice model (e.g., `en_US-lessac-medium.onnx`)

---

## ⚠️ Current Status

This is an experimental prototype exploring real-time AI voice systems.
Some features like wake word detection and latency optimization are still under development.

## 📌 Future Improvements

* Real-time streaming input
* Better wake word detection
* Memory and personalization
* Mobile integration

## 🎯 Goal

To build a fully offline, intelligent AI assistant.

---

> Built as a personal learning project to explore AI systems engineering.
