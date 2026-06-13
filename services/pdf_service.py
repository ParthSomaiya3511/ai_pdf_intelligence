import os

from config.settings import UPLOAD_DIR
from core.document_loader import DocumentLoader


class PDFService:

    @staticmethod
    def get_pdf_path(filename):

        return os.path.join(
            UPLOAD_DIR,
            filename
        )

    @staticmethod
    def load_pdf(filename):

        pdf_path = PDFService.get_pdf_path(
            filename
        )

        return DocumentLoader.load_document(
            pdf_path
        )

    @staticmethod
    def get_pdf_bytes(filename):

        pdf_path = PDFService.get_pdf_path(
            filename
        )

        with open(
            pdf_path,
            "rb"
        ) as file:

            return file.read()