# test_instagram_fields.py

from app.ingestion.instagram import (
    extract_instagram_metadata
)

data = extract_instagram_metadata(
    "https://www.instagram.com/reel/DKG8krgseWt/?hl=en"
)

print(data)

# from yt_dlp import YoutubeDL

# with YoutubeDL({"quiet": True}) as ydl:
#     info = ydl.extract_info(
#         "https://www.instagram.com/reel/DKG8krgseWt/?hl=en",
#         download=False
#     )

# print(info.keys())


