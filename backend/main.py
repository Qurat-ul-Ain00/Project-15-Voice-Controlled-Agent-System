from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

class LogEntry(BaseModel):
    agent: str
    topic: str
    message: str
    timestamp: datetime

logs = []

@app.post("/add_log/")
def add_log(entry: LogEntry):
    logs.append(entry)
    return {"message": "Log added successfully!", "log": entry}

@app.get("/get_logs/", response_model=List[LogEntry])
def get_logs():
    return logs