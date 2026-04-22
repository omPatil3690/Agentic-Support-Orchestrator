import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0
)

def intake_node(state: dict) -> dict:
    """
    LangGraph Intake Node
    Input:
        state["ticket"] : str
    Output:
        state["category"]
        state["urgency"]
    """

    ticket = state["ticket"]

    prompt = f"""
You are a customer support intake agent.

Classify the ticket below into ONE category:
- Technical
- Billing
- General

Also assign urgency from 1 (low) to 5 (high).

Ticket:
\"\"\"{ticket}\"\"\"

Respond ONLY in valid JSON like:
{{
  "category": "Technical",
  "urgency": 4
}}
"""

    response = llm.invoke(prompt)

    try:
        parsed = json.loads(response.content)#Converts JSON to dict
        state["category"] = parsed["category"]
        state["urgency"] = int(parsed["urgency"])
    except Exception:
        # Safe fallback
        state["category"] = "General"
        state["urgency"] = 3

    return state
