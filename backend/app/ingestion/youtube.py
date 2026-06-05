from yt_dlp import YoutubeDL

def extract_metadata(url: str):

    opts = {
        "quiet": True
    }

    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
    "video_id": info.get("id"),
    "title": info.get("title"),
    "creator": info.get("uploader"),
    "views": info.get("view_count"),
    "likes": info.get("like_count"),
    "comments": info.get("comment_count"),
    "duration": info.get("duration"),
    "upload_date": info.get("upload_date"),
    "thumbnail": info.get("thumbnail")
}