from app.ingestion.youtube import extract_metadata
from app.ingestion.transcript import extract_transcript


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