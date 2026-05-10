# RAG-Based Healthcare Assistant using LangGraph & HITL

A conversational healthcare assistant built using Retrieval-Augmented Generation (RAG), LangGraph, ChromaDB, HuggingFace Embeddings, and Groq LLM.

The system retrieves relevant healthcare information from medical PDF documents and generates grounded responses with conversational memory and Human-in-the-Loop (HITL) refinement.

---

## Features

- Retrieval-Augmented Generation (RAG)
- Conversational Healthcare Assistant
- LangGraph Workflow
- Human-in-the-Loop (HITL)
- Conversational Memory
- Chroma Vector Database
- PDF-based Knowledge Base

---

## Architecture

```text id="architectureflow"
User Query
    ↓
Retriever
    ↓
ChromaDB
    ↓
Relevant Chunks
    ↓
LLM (Groq)
    ↓
Generated Response
    ↓
Human Review (HITL)
Tech Stack
Python
LangChain
LangGraph
ChromaDB
HuggingFace Embeddings
Groq API
Installation
git clone https://github.com/tejassswa17/rag-healthcare-assistant.git
cd rag-healthcare-assistant

Install dependencies:

pip install -r requirements.txt

Create .env file:

GROQ_API_KEY=your_api_key

Run chatbot:

python chat.py
Example Queries
What is diabetes?
What are its symptoms?
Medicines for it
How to prevent it?
Future Enhancements
Query rewriting
Better conversational retrieval
Streamlit UI
FastAPI deployment
Long-term memory