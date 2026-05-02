# 🎙️ Voice-Controlled Agent System

A local AI voice assistant that listens to speech, understands intent, routes it to specialized agents, and responds using speech output. It also stores conversation history for memory.

---

## 🧠 Core Idea

User speaks → System converts speech to text → AI agent processes request → Response is generated → System speaks back the answer → Everything is stored in memory.

---

## 🤖 Agents

1. Task Agent: Handles to-do items and task extraction  
2. Research Agent: Answers factual or detailed questions  
3. Chat Agent: Handles general conversation  

---

## ⚙️ Features

- 🎤 Speech-to-text using Whisper (local)
- 🧠 Intent-based agent routing
- 🤖 Multi-agent system (task, research, chat)
- 🔊 Text-to-speech response
- 💾 Memory system (stores logs, audio, responses)
- 📁 Local execution (no API keys required)

---

## 🧩 Project Structure

voice-agent/
│
├── backend/
│   ├── main.py
│   ├── speech.py
│   ├── tts.py
│   ├── agents.py
│   └── memory.json
│
├── frontend/
│   └── app.py
│
├── audio_logs/
└── requirements.txt

---

## ⚙️ Setup & Run

### 1. Install dependencies
pip install -r requirements.txt

---

### 2. Install FFmpeg
sudo apt install ffmpeg

---

### 3. Install Whisper + dependencies
pip install openai-whisper

---

### 4. Install and run Ollama
Download Ollama: https://ollama.com

Pull model:
ollama pull llama2

---

## ▶️ Run Backend (FastAPI)

cd backend
uvicorn main:app --reload --port 8000

Backend runs at:
http://localhost:8000

---

## ▶️ Run Frontend (Streamlit)

cd frontend
streamlit run app.py

Frontend runs at:
http://localhost:8501

---

## 🎤 How It Works

1. User uploads a voice file (.wav)
2. Whisper converts speech → text
3. System classifies intent:
   - task
   - research
   - chat
4. Appropriate agent is selected
5. LLM generates response (via Ollama)
6. Response is spoken using TTS
7. Conversation is saved in memory

---

## 🧠 Memory System

Stores:
- User input (transcribed text)
- Agent response
- Audio file path
- Timestamp

Example:

{
  "timestamp": "2026-01-01 10:00:00",
  "input": "What are my tasks today?",
  "response": "You need to complete project report and attend meeting.",
  "audio": "audio_logs/file1.wav"
}

---

## 🧾 API Endpoints

### Voice Processing
POST /voice/

Request:
- Audio file (.wav)

Response:
{
  "input_text": "...",
  "response": "..."
}

---

## 🔊 Output System

- Uses pyttsx3 for offline text-to-speech
- Speaks responses in real-time after processing

---

## ⚠️ Limitations

- Whisper is slow on CPU
- Voice quality depends on TTS engine
- Intent classification may misroute queries
- No real-time streaming (file-based input only)

---

## 🚀 Future Improvements

- Real-time microphone input
- Streaming voice responses
- Better TTS (Coqui AI)
- Conversation memory context window
- Multi-speaker detection
- Mobile app version

---

## 💡 Tech Stack

- FastAPI (backend)
- Streamlit (frontend)
- Whisper (speech-to-text)
- Ollama + LLaMA 2 (LLM)
- pyttsx3 (text-to-speech)
- Python (core language)

---

## 📜 License

This project is open-source and free to use.