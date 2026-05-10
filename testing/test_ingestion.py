from src.ingestion.pipeline import IngestionPipeline

pipeline = IngestionPipeline("data/Medical_book.pdf")
chunks = pipeline.run()

print(f"Total chunks: {len(chunks)}")
print(chunks[:3])