from app.ingestion.youtube import extract_metadata
from app.ingestion.transcript import extract_transcript
from app.ingestion.instagram import (
    extract_instagram_metadata
)

from app.ingestion.instagram_transcript import (
    extract_instagram_transcript
)

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

def process_video(url: str):

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

    return {
        "metadata": metadata,
        "transcript": transcript
    }