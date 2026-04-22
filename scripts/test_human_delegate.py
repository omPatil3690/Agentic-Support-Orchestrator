from ..agents.human_delegate import human_delegate_node

# Mock state as it would come from the solver with low confidence
state = {
    "ticket": "My account is locked and I tried everything",
    "confidence": 0.25,
    "plan": ["Tried automated recovery steps but failed"]
}

updated_state = human_delegate_node(state)

print("\n--- UPDATED STATE ---\n")
print(updated_state)

print("\n--- FINAL ANSWER ---\n")
print(updated_state["final_answer"])

print("\n--- ESCALATION STATUS ---\n")
print("Escalated:", updated_state["escalated"])