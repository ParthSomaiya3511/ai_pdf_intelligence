from database.chromadb_manager import (
    ChromaDBManager
)

from ai.llm_manager import (
    LLMManager
)


class RAGPipeline:

    @staticmethod
    def build():

        db = (
            ChromaDBManager
            .load_vector_store()
        )

        retriever = db.as_retriever(
            search_kwargs={
                "k": 5
            }
        )

        llm = (
            LLMManager.get_llm()
        )

        return retriever, llm