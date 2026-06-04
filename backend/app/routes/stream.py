from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.stream import (
    StreamRequest
)

from app.rag.streaming import (
    stream_response
)

router = APIRouter()


@router.post("/stream")
def stream(
    request: StreamRequest
):

    prompt = f"""
Answer this question:

{request.question}
"""

    return StreamingResponse(
        stream_response(prompt),
        media_type="text/plain"
    )