from src.workflow.graph import build_graph

app = build_graph()

query = "What are symptoms of diabetes?"

result = app.invoke({
    "query": query,
    "context": [],
    "answer": "",
    "escalate": False
})

print("\nFinal Answer:\n")
print(result["answer"])

print("\nEscalation:", result["escalate"])