from ..tools.serper_tool import google_serper_search

def tool_agent(state: dict) -> dict:
    """
    Uses tools when solver confidence is low.
    """

    ticket = state["ticket"]

    external_info = google_serper_search(ticket)

    state["tool_context"] = (
        "External search results:\n" + external_info
    )

    return state
