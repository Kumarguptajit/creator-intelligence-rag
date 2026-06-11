from app.ingestion.instagram import (
    extract_instagram_metadata
)

from app.ingestion.downloader import (
    download_audio
)

from app.ingestion.audio_transcript import (
    transcribe_audio
)
import time

def extract_instagram_transcript(
    url: str,
    metadata: dict
):
    
    description = metadata.get(
        "description",
        ""
    )

    try:

        download_start = time.time()

        audio_file = download_audio(
            url
        )

        print(
            f"Audio download took "
            f"{time.time() - download_start:.2f}s"
        )

        transcribe_start = time.time()

        transcript = transcribe_audio(
            audio_file
        )

        print(
            f"Whisper transcription took "
            f"{time.time() - transcribe_start:.2f}s"
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