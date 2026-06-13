import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "uploads"
)

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)