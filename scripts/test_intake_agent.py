from ..agents.intake import intake_node

state = {
    "ticket": "My account is locked and I cannot login"
}

updated_state = intake_node(state)

print(updated_state)