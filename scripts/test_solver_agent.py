from ..agents.solver import solve

state = {
    "ticket": "My account is locked and I cannot login",
    "category": "Technical",
    "urgency": 4,
    "context": [
        "Account Locked Due to Multiple Failed Login Attempts...",
        "Password Reset Not Working..."
    ]
}

updated_state = solve(state)

print("Plan:")
for step in updated_state["plan"]:
    print("-", step)

print("\nConfidence:", updated_state["confidence"])
