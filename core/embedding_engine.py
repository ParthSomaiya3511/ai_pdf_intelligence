from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)


class EmbeddingEngine:

    @staticmethod
    def get_embeddings():

        return HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )