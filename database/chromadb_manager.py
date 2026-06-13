from langchain_chroma import Chroma

from core.embedding_engine import (
    EmbeddingEngine
)


class ChromaDBManager:

    @staticmethod
    def create_vector_store(
        documents
    ):

        embeddings = (
            EmbeddingEngine.get_embeddings()
        )

        db = Chroma(
            persist_directory="vector_db",
            embedding_function=embeddings
        )

        db.add_texts(
            texts=documents
        )

        return db

    @staticmethod
    def load_vector_store():

        embeddings = (
            EmbeddingEngine.get_embeddings()
        )

        return Chroma(
            persist_directory="vector_db",
            embedding_function=embeddings
        )