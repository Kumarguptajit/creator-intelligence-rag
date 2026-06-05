from app.ingestion.instagram import extract_instagram_metadata

INSTAGRAM_REEL_URL = "https://www.instagram.com/reel/DY32H6BINDH/?igsh=MTFzY25heXZxOHF3bg=="
data = extract_instagram_metadata(
    INSTAGRAM_REEL_URL
)

print(data)