from fastapi import APIRouter

from app.schemas.chat import ChatRequest

from app.services.chat_service import (
    answer_question
)

router = APIRouter()


@router.post("/chat")
def chat(
    request: ChatRequest
):

    answer = answer_question(
        request.question
    )

    return {
        "answer": answer
    }