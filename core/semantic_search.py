from database.chromadb_manager import (
    ChromaDBManager
)


class SemanticSearch:

    @staticmethod
    def search(
        query,
        k=5
    ):

        db = (
            ChromaDBManager
            .load_vector_store()
        )

        results = (
            db.similarity_search(
                query,
                k=k
            )
        )

        return results