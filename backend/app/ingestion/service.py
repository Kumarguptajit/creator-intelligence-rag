from importlib import metadata
import time
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
    start_total = time.time()

    if "instagram.com" in url:

        metadata = extract_instagram_metadata(
            url
        )
        transcript_start = time.time()
        transcript = extract_instagram_transcript(
            url,
            metadata
        )
        print(
            f"Transcript extraction took "
            f"{time.time() - transcript_start:.2f}s"
        )

    else:

        metadata = extract_metadata(
            url
        )
        transcript_start = time.time()
        transcript = extract_transcript(
            url,
            metadata
        )
        print(
            f"Transcript extraction took "
            f"{time.time() - transcript_start:.2f}s"
        )
    metadata["engagement_rate"] = (
        calculate_engagement_rate(
            metadata.get("views"),
            metadata.get("likes"),
            metadata.get("comments")
        )
    )
    chunk_start = time.time()
    chunks = chunk_text(
        transcript,
        metadata["video_id"],
        video_label
    )

    print(
        f"Chunking took "
        f"{time.time() - chunk_start:.2f}s"
    )
    print(f"Created {len(chunks)} chunks")

    embed_start = time.time()

    embedded_chunks = embed_chunks(
        chunks
    )

    print(
        f"Embedding took "
        f"{time.time() - embed_start:.2f}s"
    )

    store_start = time.time()

    store_chunks(
        embedded_chunks
    )

    print(
        f"Qdrant storage took "
        f"{time.time() - store_start:.2f}s"
    )

    print(
        f"Total processing time: "
        f"{time.time() - start_total:.2f}s"
    )

    return {
        "metadata": metadata,
        "transcript": transcript
    }