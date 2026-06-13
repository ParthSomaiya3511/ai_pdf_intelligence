import os

from config.settings import UPLOAD_DIR


class UploadService:

    @staticmethod
    def save_file(uploaded_file):

        file_path = os.path.join(
            UPLOAD_DIR,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return file_path

    @staticmethod
    def get_uploaded_files():

        files = []

        if os.path.exists(UPLOAD_DIR):

            for file in os.listdir(UPLOAD_DIR):

                if file.lower().endswith(".pdf"):
                    files.append(file)

        return files