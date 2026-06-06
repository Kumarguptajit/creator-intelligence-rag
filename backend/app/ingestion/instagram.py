from yt_dlp import YoutubeDL
import requests
import re


def extract_follower_count(username):

    response = requests.get(
        f"https://www.instagram.com/{username}/",
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    html = response.text

    match = re.search(
        r'([0-9.,]+[MK]?) Followers',
        html,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return None


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

    creator = (
        info.get("channel")
        or info.get("uploader")
    )

    follower_count = None

    if creator:
        follower_count = extract_follower_count(
            creator
        )

    return {
        "video_id": info.get("id"),
        "title": info.get("title"),
        "creator": creator,
        "follower_count": follower_count,
        "views": info.get("view_count"),
        "likes": info.get("like_count"),
        "comments": info.get("comment_count"),
        "duration": info.get("duration"),
        "upload_date": info.get("upload_date"),
        "thumbnail": info.get("thumbnail"),
        "description": description,
        "hashtags": hashtags
    }