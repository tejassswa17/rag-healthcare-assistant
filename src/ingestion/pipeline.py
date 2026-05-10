from src.ingestion.loader import PDFLoader
from src.ingestion.chunker import TextChunker


class IngestionPipeline:
    def __init__(self, file_path):
        self.loader = PDFLoader(file_path)
        self.chunker = TextChunker()

    def run(self):
        # Step 1: Load PDF
        text = self.loader.load()

        # Step 2: Split into chunks
        chunks = self.chunker.split(text)

        return chunks