from src.ingestion.pipeline import IngestionPipeline
from src.retrieval.vector_store import VectorStore

# Step 1: Load + chunk
pipeline = IngestionPipeline("data/Medical_book.pdf")
chunks = pipeline.run()

print("Chunks ready:", len(chunks))

# Step 2: Store in vector DB
store = VectorStore()
vectordb = store.create_store(chunks)

print("Vector DB created successfully")