from ..agents.responder import responder

# Mock state as it would come from solver
state = {
    "plan": [
        "Verify the user's identity",
        "Unlock the account from the admin dashboard",
        "Send a password reset email",
        "Ask the user to login again"
    ],
    "confidence": 0.82
}

updated_state = responder(state)

print("\n--- UPDATED STATE ---\n")
print(updated_state)

print("\n--- FINAL ANSWER ---\n")
print(updated_state["final_answer"])
