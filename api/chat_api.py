from fastapi import (
    APIRouter
)

from pydantic import (
    BaseModel
)

from services.chat_service import (
    ChatService
)

router = APIRouter(
    prefix="/chat"
)


class ChatRequest(
    BaseModel
):
    question: str


@router.post("/")
def chat(
    request:
    ChatRequest
):

    result = (
        ChatService.ask(
            request.question
        )
    )

    return result