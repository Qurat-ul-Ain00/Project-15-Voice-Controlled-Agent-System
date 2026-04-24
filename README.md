# Agent Collaboration Timeline

This project visualizes the sequence of agent outputs over time in a timeline view. It consists of two main components:

1. **Backend**: A FastAPI application to handle log storage and retrieval.
2. **Frontend**: A Streamlit application to display the timeline and logs.

## Features

- Add timestamps to all agent logs.
- Render agent responses on a visual timeline.
- Group interactions by agent and topic.
- Export the timeline as a PDF or PNG for reporting.

## Project Structure

```
agent-collaboration-timeline/
│
├── backend/
│   └── main.py          # FastAPI backend
│
├── frontend/
│   └── app.py           # Streamlit frontend
│
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agent-collaboration-timeline
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Backend

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Exporting Timeline

- The timeline can be exported as a PDF or PNG for reporting purposes (feature under development).

## License

This project is licensed under the MIT License.