# backend/app/routes/context.py

from fastapi import APIRouter

from app.rag.comparison_context import (
    get_comparison_context
)

router = APIRouter()


@router.get("/comparison-context")
def comparison_context():

    comparison = get_comparison_context()

    print("COMPARISON CONTEXT:")
    print(comparison)

    return {
        "video_a": comparison.get(
            "metadata_a",
            {}
        ),
        "video_b": comparison.get(
            "metadata_b",
            {}
        )
    }