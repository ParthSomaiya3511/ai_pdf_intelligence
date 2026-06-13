from core.pdf_parser import PDFParser


class DocumentLoader:

    @staticmethod
    def load_document(pdf_path):

        return {
            "text": PDFParser.extract_text(pdf_path),
            "pages": PDFParser.get_page_count(pdf_path),
            "metadata": PDFParser.get_metadata(pdf_path)
        }