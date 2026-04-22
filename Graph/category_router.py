def category_router(state: dict) -> str:
    """
    Routes based on ticket category.
    """

    category = state.get("category", "General")

    if category == "General":
        return "general_responder"

    # Technical or Billing
    return "retriever"
