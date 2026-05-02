import requests

def call_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

def classify_intent(text):
    prompt = f"""
    Classify the intent:
    '{text}'

    Options:
    - task
    - research
    - chat

    Return only one word.
    """
    return call_ollama(prompt).strip().lower()

def task_agent(text):
    return call_ollama(f"Extract and manage task from: {text}")

def research_agent(text):
    return call_ollama(f"Provide detailed answer: {text}")

def chat_agent(text):
    return call_ollama(f"Respond conversationally: {text}")

def route(text):
    intent = classify_intent(text)

    if "task" in intent:
        return task_agent(text)
    elif "research" in intent:
        return research_agent(text)
    else:
        return chat_agent(text)