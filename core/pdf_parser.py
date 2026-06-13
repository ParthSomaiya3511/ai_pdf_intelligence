import fitz


class PDFParser:

    @staticmethod
    def extract_text(pdf_path):

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    @staticmethod
    def get_page_count(pdf_path):

        document = fitz.open(pdf_path)

        count = len(document)

        document.close()

        return count

    @staticmethod
    def get_metadata(pdf_path):

        document = fitz.open(pdf_path)

        metadata = document.metadata

        document.close()

        return metadata