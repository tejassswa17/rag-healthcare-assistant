from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


class Retriever:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            persist_directory="chroma_db",
            embedding_function=self.embedding
        )

    def search(self, query, k=5):
        results = self.db.similarity_search(query, k=k)
        return [doc.page_content for doc in results]