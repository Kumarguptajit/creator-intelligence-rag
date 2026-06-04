from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.compare import (
    CompareRequest
)

from app.services.comparison_service import (
    prepare_comparison
)

from app.rag.streaming import (
    stream_response
)

router = APIRouter()

@router.post("/compare")
def compare_videos(
    request: CompareRequest
):

    prompt = prepare_comparison(
        request.video_a_url,
        request.video_b_url
    )

    return StreamingResponse(
        stream_response(prompt),
        media_type="text/plain"
    )