# # Mock user history store
# # Later replace with DB / Redis

# USER_HISTORY_DB = {
#     "user_001": [
#         {
#             "issue": "account_locked",
#             "resolution": "password_reset_sent",
#             "escalated": False
#         }
#     ]
# }

# def get_user_history(user_id: str) -> str:
#     """
#     Fetch past support history for a user.
#     """

#     history = USER_HISTORY_DB.get(user_id)

#     if not history:
#         return "No previous support history found."

#     summary = "User support history:\n"
#     for record in history:
#         summary += (
#             f"- Issue: {record['issue']}, "
#             f"Resolution: {record['resolution']}, "
#             f"Escalated: {record['escalated']}\n"
#         )

#     return summary
