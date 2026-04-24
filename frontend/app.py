import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Streamlit app
st.title("Agent Collaboration Timeline")

# Fetch logs from backend
response = requests.get("http://127.0.0.1:8000/get_logs/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Group by agent and topic
    grouped = df.groupby(['agent', 'topic'])

    # Render timeline
    st.header("Timeline")
    fig, ax = plt.subplots(figsize=(10, 6))
    for (agent, topic), group in grouped:
        ax.plot(group['timestamp'], [f"{agent} - {topic}" for _ in group['timestamp']], 'o-', label=f"{agent} - {topic}")

    ax.set_yticks([f"{agent} - {topic}" for agent, topic in grouped.groups.keys()])
    ax.set_xlabel("Time")
    ax.set_ylabel("Agent - Topic")
    ax.legend()
    st.pyplot(fig)

    # Display data
    st.header("Agent Logs")
    st.dataframe(df)
else:
    st.error("Failed to fetch logs from the backend.")