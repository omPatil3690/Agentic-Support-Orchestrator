from ..agents.retrieval_agent import retrieve_documents

state = {
    "ticket": "My account is locked and I cannot login",
    "category": "Technical",
    "urgency": 4
}

updated_state = retrieve_documents(state)

print("Retrieved context:\n")
for doc in updated_state["context"]:
    print("-----")
    print(doc)
