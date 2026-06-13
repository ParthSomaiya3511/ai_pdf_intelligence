from fastapi import FastAPI

from api.search_api import (
    router as search_router
)

from api.chat_api import (
    router as chat_router
)

app = FastAPI(
    title="AI PDF Intelligence API"
)

app.include_router(
    search_router
)

app.include_router(
    chat_router
)