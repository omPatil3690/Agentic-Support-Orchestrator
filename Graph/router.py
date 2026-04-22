def router(state: dict) -> str:
    """
    Routes based on confidence and tool usage
    """

    confidence = state.get("confidence", 0)
    tool_context = state.get("tool_context")  # SAFE

    if confidence < 0.6 and not tool_context:
        return "tool_node"

    if confidence < 0.6 and tool_context:
        return "human_delegate"

    return "responder"
