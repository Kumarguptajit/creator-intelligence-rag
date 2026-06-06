from app.ingestion.youtube import extract_metadata
from app.ingestion.transcript import extract_transcript
from app.ingestion.instagram import (
    extract_instagram_metadata
)

from app.ingestion.instagram_transcript import (
    extract_instagram_transcript
)
from app.rag.chunker import chunk_text
from app.rag.embeddings import  embed_chunks
from app.vectorstore.vector_store import store_chunks
from app.rag.chunker import chunk_text

def calculate_engagement_rate(
    views,
    likes,
    comments
):
    if not views:
        return 0

    return round(
        ((likes or 0) + (comments or 0))
        / views * 100,
        2
    )


def process_youtube_video(url: str):

    metadata = extract_metadata(url)

    metadata["engagement_rate"] = calculate_engagement_rate(
        metadata["views"],
        metadata["likes"],
        metadata["comments"]
    )

    transcript = extract_transcript(url)

    return {
        "metadata": metadata,
        "transcript": transcript
    }

def process_video(url: str, video_label: str):

    if "instagram.com" in url:

        metadata = extract_instagram_metadata(
            url
        )

        transcript = extract_instagram_transcript(
            url
        )

    else:

        metadata = extract_metadata(
            url
        )

        transcript = extract_transcript(
            url
        )

        metadata["engagement_rate"] = (
            calculate_engagement_rate(
                metadata.get("views"),
                metadata.get("likes"),
                metadata.get("comments")
            )
        )

        chunks = chunk_text(
            transcript,
            metadata["video_id"],
            video_label
        )

        embedded_chunks = embed_chunks(
            chunks
        )

        store_chunks(
            embedded_chunks
        )



    return {
        "metadata": metadata,
        "transcript": transcript
    }