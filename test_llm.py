from src.retrieval.retriever import Retriever
from src.llm.llm import LLMModel

retriever = Retriever()
llm = LLMModel()

query = "What are symptoms of diabetes?"

# Step 1: Retrieve context
results = retriever.search(query)
context = "\n".join(results)

# Step 2: Generate answer
answer = llm.generate(query, context)

print("Answer:\n")
print(answer)