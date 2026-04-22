from typing import Dict
from ..agents.tool_agent import tool_agent
from ..agents.intake import intake_node
from ..agents.retrieval_agent import retrieve_documents
from ..agents.solver import solve
from ..agents.responder import responder
from ..agents.human_delegate import human_delegate_node
from ..agents.general_responder import general_responder

from .support_state import State
from .router import router
from .category_router import category_router

from langgraph.graph import StateGraph, END


def build_graph():
    graph = StateGraph(State)

    # Add nodes
    graph.add_node("intake", intake_node)
    graph.add_node("general_responder", general_responder)
    graph.add_node("retriever", retrieve_documents)
    graph.add_node("solver", solve)
    graph.add_node("tool_node", tool_agent)
    graph.add_node("responder", responder)
    graph.add_node("human_delegate", human_delegate_node)

    # Entry point
    graph.set_entry_point("intake")

    graph.add_conditional_edges(
        "intake",
        category_router,
        {
            "general_responder": "general_responder",
            "retriever": "retriever",
        }
    )

    # Technical / Billing flow
    graph.add_edge("retriever", "solver")

    graph.add_conditional_edges(
        "solver",
        router,
        {
            "tool_node": "tool_node",
            "responder": "responder",
            "human_delegate": "human_delegate",
        }
    )

    # Tool loop
    graph.add_edge("tool_node", "solver")

    # End states
    graph.add_edge("general_responder", END)
    graph.add_edge("responder", END)
    graph.add_edge("human_delegate", END)

    return graph.compile()
