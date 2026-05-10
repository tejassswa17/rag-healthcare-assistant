from langchain_community.embeddings import HuggingFaceEmbeddings


class EmbeddingModel:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

    def embed(self, texts):
        return self.model.embed_documents(texts)