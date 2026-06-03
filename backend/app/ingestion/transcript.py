from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def get_video_id(url: str) -> str:
    parsed = urlparse(url)

    if parsed.hostname in ["youtube.com", "www.youtube.com"]:
        return parse_qs(parsed.query)["v"][0]

    if parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/")

    raise ValueError("Invalid YouTube URL")


def extract_transcript(url: str):

    video_id = get_video_id(url)

    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video_id)

    text = " ".join(
        snippet.text
        for snippet in transcript
    )

    return text