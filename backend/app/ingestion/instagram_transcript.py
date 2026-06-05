from app.ingestion.instagram import (
    extract_instagram_metadata
)

from app.ingestion.downloader import (
    download_audio
)

from app.ingestion.audio_transcript import (
    transcribe_audio
)


def extract_instagram_transcript(
    url: str
):

    metadata = extract_instagram_metadata(
        url
    )

    description = metadata.get(
        "description",
        ""
    )

    try:

        audio_file = download_audio(
            url
        )

        transcript = transcribe_audio(
            audio_file
        )

        if transcript and len(transcript) > 30:

            return transcript

        print(
            "Using description fallback"
        )

        return description

    except Exception as e:

        print(
            f"Instagram transcript error: {e}"
        )

        return description