from yt_dlp import YoutubeDL
import re


def extract_instagram_metadata(url: str):

    opts = {
        "quiet": True
    }

    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(
            url,
            download=False
        )

    description = info.get(
        "description",
        ""
    )

    hashtags = re.findall(
        r"#\w+",
        description
    )

    return {
        "video_id": info.get("id"),
        "title": info.get("title"),
        "creator": (
            info.get("channel")
            or info.get("uploader")
        ),
        "views": info.get("view_count"),
        "likes": info.get("like_count"),
        "comments": info.get("comment_count"),
        "duration": info.get("duration"),
        "upload_date": info.get("upload_date"),
        "thumbnail": info.get("thumbnail"),
        "description": description,
        "hashtags": hashtags
    }