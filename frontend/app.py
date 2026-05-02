import streamlit as st
import requests

st.title("🎙️ Voice Agent System")

audio = st.file_uploader("Upload voice (.wav)", type=["wav"])

if audio:
    if st.button("Send to Agent"):
        res = requests.post(
            "http://localhost:8000/voice/",
            files={"file": audio}
        )
        data = res.json()

        st.write("🗣️ You said:", data["input_text"])
        st.write("🤖 Agent:", data["response"])