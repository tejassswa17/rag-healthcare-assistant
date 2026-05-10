from src.retrieval.retriever import Retriever

retriever = Retriever()

query = "What are symptoms of diabetes?"
results = retriever.search(query)

print("Top results:\n")
for r in results:
    print("-", r[:200])