from fastapi import FastAPI, UploadFile, File
import tempfile
import json
import os
from datetime import datetime

from speech import transcribe
from agents import route
from tts import speak

app = FastAPI()

MEMORY_FILE = "backend/memory.json"

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)

@app.post("/voice/")
async def voice_agent(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        audio_path = tmp.name

    user_text = transcribe(audio_path)
    response = route(user_text)

    # Speak response
    speak(response)

    # Save memory
    mem = load_memory()

    entry = {
        "timestamp": str(datetime.now()),
        "audio": audio_path,
        "input": user_text,
        "response": response
    }

    mem.setdefault("logs", []).append(entry)
    save_memory(mem)

    return {
        "input_text": user_text,
        "response": response
    }