from ai.rag_pipeline import (
    RAGPipeline
)


class AIChat:

    @staticmethod
    def ask(question):

        retriever, llm = (
            RAGPipeline.build()
        )

        docs = retriever.invoke(
            question
        )

        context = "\n\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )

        prompt = f"""
You are an AI assistant.

Answer only using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

        response = llm.invoke(
            prompt
        )

        answer = (
            response.content
            if hasattr(response, "content")
            else str(response)
        )

        return {
            "answer": answer,
            "documents": docs
        }