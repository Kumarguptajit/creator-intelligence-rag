from yt_dlp import YoutubeDL

def extract_metadata(url: str):

    opts = {
        "quiet": True
    }

    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
    "title": info.get("title"),
    "creator": info.get("uploader"),
    "views": info.get("view_count"),
    "likes": info.get("like_count"),
    "comments": info.get("comment_count"),
    "duration": info.get("duration"),
    "upload_date": info.get("upload_date")
}