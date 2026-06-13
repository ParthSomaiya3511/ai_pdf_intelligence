from services.chunk_service import (
    ChunkService
)

from database.chromadb_manager import (
    ChromaDBManager
)

from core.embedding_engine import (
    EmbeddingEngine
)

from langchain_chroma import Chroma

class VectorService:

    @staticmethod
    def create_embeddings(filename):

        chunks = (
            ChunkService.generate_chunks(
                filename
            )
        )

        embeddings = (
            EmbeddingEngine.get_embeddings()
        )

        metadatas = []

        for index, chunk in enumerate(
            chunks
        ):

            metadatas.append(
                {
                    "source": filename,
                    "chunk": index
                }
            )

        Chroma.from_texts(
            texts=chunks,
            metadatas=metadatas,
            embedding=embeddings,
            persist_directory="vector_db"
        )