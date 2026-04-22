def responder(state:dict)->dict:
    """
    Takes out plan from the state and simply formats it to give response to the user
    """
    plan = state["plan"]

    response = "Here is how you can resolve your issue\n\n"
    for i,step in enumerate(plan,1):
        response += f"{step}\n"

    state["final_answer"] = response
    state["escalated"] = False

    return state