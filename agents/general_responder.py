def general_responder(state: dict) -> dict:
    """
    Handles out-of-scope / general questions.
    """

    state["final_answer"] = (
        "Thanks for reaching out!\n\n"
        "I’m currently designed to help with Technical and Billing-related issues "
        "such as account access, password problems, subscriptions, and payments.\n\n"
        "For general questions like careers, company information, or partnerships, "
        "please visit the relevant section on our website or contact the appropriate team.\n\n"
        "If you have a Technical or Billing issue, feel free to ask — I’m happy to help😊!"
    )

    state["escalated"] = False
    state["confidence"] = 0.9

    return state
