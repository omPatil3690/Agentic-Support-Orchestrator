# 📌 Agentic Support Orchestrator

An **agentic AI-based customer support system** that handles **Technical and Billing** queries using **LangGraph**, **RAG**, and **LLMs**, exposed via a **FastAPI backend** and **Streamlit UI**.

---

## 🚀 What it Does

- Classifies incoming support tickets
- Retrieves relevant knowledge base context (RAG)
- Generates clear, step-by-step resolutions
- Uses confidence-based decision routing
- Provides a clean UI for user interaction

---

## 🧠 Architecture

User Query->IntakeAgent->Router(Technical/Billing or General)->Knowledge Base(RAG) ->Solver Agent->Responder

---

## 🛠 Tech Stack

- **Python**
- **LangGraph**
- **FastAPI**
- **Streamlit**
- **ChromaDB**
- **UV** (dependency management)

---

## ▶️ Run Locally

```bash
uv sync
uvicorn api.main:app --reload
streamlit run ui/app.py


```
