from ..tools.user_history_tool import get_user_history

# Case 1: User with existing history
print("\n--- USER WITH HISTORY ---\n")
user_id_with_history = "user_001"
history = get_user_history(user_id_with_history)
print(history)

# Case 2: User with no history
print("\n--- USER WITH NO HISTORY ---\n")
user_id_no_history = "user_999"
history = get_user_history(user_id_no_history)
print(history)
