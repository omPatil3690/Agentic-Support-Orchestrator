from ..Graph.support_graph import build_graph

graph = build_graph()

final_state = graph.invoke({
    "ticket": "My invoice was generated but I didn’t receive it.Is this a known issue today?"
})

print("\n--- FINAL ANSWER ---\n")
print(final_state["final_answer"])
print("\nEscalated:", final_state["escalated"])
print("Confidence:", final_state.get("confidence"))
