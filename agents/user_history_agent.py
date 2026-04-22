# from tools.user_history_tool import get_user_history

# def user_history_node(state: dict) -> dict:
#     """
#     LangGraph node to fetch per-user memory.
#     """

#     user_id = state.get("user_id")

#     if not user_id:
#         state["user_history"] = "User not identified."
#         return state

#     state["user_history"] = get_user_history(user_id)
#     return state
