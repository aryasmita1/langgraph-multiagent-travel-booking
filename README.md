# langgraph-multiagent-travel-booking

A Multi-Agent AI Travel Booking System built using LangGraph, LangChain, Groq LLM, Streamlit, PostgreSQL, Tavily Search, and AviationStack APIs. The application leverages multiple AI agents to collaboratively generate complete travel plans by retrieving flight information, hotel recommendations, and creating personalized travel itineraries.

## Live Demo

https://langgraph-multiagent-travel-booking-aryasmita1.streamlit.app/

## Features

- Multi-Agent workflow powered by LangGraph
- Flight information retrieval using AviationStack API
- Hotel search using Tavily AI Search
- AI-generated personalized travel itineraries
- Conversation memory using PostgreSQL Checkpointer
- Streamlit-based interactive user interface
- Groq Llama 3.3 70B model integration
- Modular and scalable agent architecture

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python
- LangGraph
- LangChain

### AI Model
- Groq
- Llama 3.3 70B Versatile

### Database
- PostgreSQL

### APIs
- Tavily Search API
- AviationStack API

### Environment Management
- Python Virtual Environment
- python-dotenv

---

## Project Architecture

```
User Query
      │
      ▼
Flight Agent
      │
      ▼
Hotel Agent
      │
      ▼
Itinerary Agent
      │
      ▼
Final Response Agent
      │
      ▼
Travel Plan
```

The workflow is managed by LangGraph while PostgreSQL stores conversation checkpoints to maintain persistent memory across sessions.

---

## Workflow

1. User enters a travel request.
2. Flight Agent retrieves available flight information.
3. Hotel Agent searches for hotels relevant to the destination.
4. Itinerary Agent combines all retrieved information.
5. Groq LLM generates a personalized travel itinerary.
6. Final Agent prepares the complete travel response.
7. PostgreSQL stores the conversation state.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/aryasmita1/langgraph-multiagent-travel-booking.git
```

```bash
cd langgraph-multiagent-travel-booking
```

### Create Virtual Environment

```bash
python -m venv langgraph_env
```

### Activate Virtual Environment

Windows

```bash
langgraph_env\Scripts\activate
```

Linux / macOS

```bash
source langgraph_env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key
DATABASE_URL=your_postgresql_connection_string
```

---

## Run the Project

```bash
streamlit run app.py
```

or

```bash
python main.py
```

---

## Project Structure

```
langgraph-multiagent-travel-booking/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env
│
├── tools/
│   ├── flight_tool.py
│   └── tavily_tool.py
│
└── ...
```

---

## Future Enhancements

- Real-time flight booking
- Hotel booking integration
- Weather forecasting
- Budget optimization
- Google Maps integration
- Multi-city trip planning
- PDF itinerary generation
- Voice-enabled travel assistant
- Authentication and user profiles
- Booking history and recommendations

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Multi-Agent AI Systems
- LangGraph State Graphs
- Agent-based Workflow Design
- LangChain Integration
- LLM Orchestration
- PostgreSQL Checkpointing
- API Integration
- Prompt Engineering
- Streamlit Deployment
- Cloud-based AI Application Development

---

## Author

Aryasmita

GitHub: https://github.com/aryasmita1
