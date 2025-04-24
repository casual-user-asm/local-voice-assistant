# Voice Assistant – Local AI Chat with Speech
A simple and privacy-friendly voice assistant that runs entirely on your local machine. It uses powerful open-source tools for speech recognition, text-to-speech, and AI conversation — with no cloud dependencies.

## 🧩 Features

- 🎙️ Voice input using OpenAI Whisper
- 🧠 Text generation using local LLMs via Ollama
- 🔊 Text-to-Speech with Coqui.ai
- 🔐 100% local — no data leaves your machine

---

## 🚀 Quick Start

### 1. Install dependencies

Make sure Python 3.8+ is installed.

```bash
pip install -r requirements.txt
```
You’ll also need:

 - Ollama for local LLMs

 - ffmpeg and sox (check your system’s package manager)

### 2. Start Ollama with a model(choose any model you like -> https://ollama.com/search)

```bash
ollama run gemma3
```

### 3. Activate virtual environment in terminal

```bash
venv\Scripts\activate
```

### 4. Run the assistant

```bash
python main.py
```
