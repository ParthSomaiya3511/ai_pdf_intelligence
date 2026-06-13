from core.chunking_engine import (
    ChunkingEngine
)

from services.pdf_service import (
    PDFService
)


class ChunkService:

    @staticmethod
    def generate_chunks(filename):

        pdf_data = PDFService.load_pdf(
            filename
        )

        text = pdf_data["text"]

        engine = ChunkingEngine()

        chunks = engine.split_text(
            text
        )

        return chunks