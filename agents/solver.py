import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0
)

def solve(state: dict) -> dict:
    """
    LangGraph Solver Node

    Input:
        state["ticket"]
        state["context"]
        state.get("user_history")
        state.get("tool_context")

    Output:
        state["plan"]
        state["confidence"]
    """

    ticket = state["ticket"]
    context = "\n\n".join(state.get("context", []))
    # user_history = state.get("user_history", "No prior user history.")
    tool_context = state.get("tool_context", "No external information used.")

    prompt = f"""
You are a senior customer support resolution agent.

User issue:
{ticket}

Internal knowledge base:
{context}

Additional external information:
{tool_context}

Based on ALL the above information, create a clear step-by-step resolution plan.

Also estimate your confidence in this solution as a number between 0 and 1.

Respond ONLY in valid JSON like:
{{
  "plan": [
    "Step 1 ...",
    "Step 2 ..."
  ],
  "confidence": 0.85
}}
"""

    response = model.invoke(prompt)

    try:
        parsed = json.loads(response.content)
        state["plan"] = parsed["plan"]
        state["confidence"] = float(parsed["confidence"])
    except Exception:
        state["plan"] = ["Escalate to human support"]
        state["confidence"] = 0.3

    return state
