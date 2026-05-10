from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorStore:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

    def create_store(self, texts):
        vectordb = Chroma.from_texts(
            texts=texts,
            embedding=self.embedding,
            persist_directory="chroma_db"
        )
        return vectordb