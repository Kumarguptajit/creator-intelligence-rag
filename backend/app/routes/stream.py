from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.stream import StreamRequest

from app.rag.streaming import (
    stream_response
)

from app.rag.comparison_context import (
    get_comparison_context
)

router = APIRouter()


@router.post("/stream")
def stream(request: StreamRequest):

    comparison = get_comparison_context()

    prompt = f"""
You are a creator intelligence analyst.

Comparison Context:
{comparison}

IMPORTANT:

If comparison context exists:

- Assume the user refers to Video A and Video B.
- Never ask for the videos again.
- Never say you cannot access the videos.
- Use transcript context as the primary source.
- Do not rely solely on metadata.
- Support claims with transcript evidence.
- Explain performance using:
  - hook
  - structure
  - engagement
  - educational value
  - audience appeal

Question:
{request.question}
"""

    return StreamingResponse(
        stream_response(prompt),
        media_type="text/plain"
    )