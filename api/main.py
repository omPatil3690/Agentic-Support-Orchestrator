from fastapi import FastAPI
from pydantic import BaseModel
from ..Graph.support_graph import build_graph

# Build graph once (important for performance)
graph = build_graph()

app = FastAPI(
    title="Agentic Support Orchestrator",
    description="KB-first, tool-augmented support system using LangGraph",
    version="1.0.0"
)

# -------- Request / Response Schemas --------

class SupportRequest(BaseModel):
    ticket: str

class SupportResponse(BaseModel):
    answer: str
    escalated: bool
    confidence: float | None = None
    tool_used: bool = False


# -------- API Endpoint --------

@app.post("/support/query", response_model=SupportResponse)
def support_query(request: SupportRequest):
    """
    Main support endpoint
    """

    final_state = graph.invoke({
        "ticket": request.ticket
    })

    return {
        "answer": final_state.get("final_answer", ""),
        "escalated": final_state.get("escalated", False),
        "confidence": final_state.get("confidence"),
        "tool_used": final_state.get("tool_used", False),
    }
