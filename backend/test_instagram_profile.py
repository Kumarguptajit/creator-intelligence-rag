import requests
import re

username = "madhuridixitnene"

response = requests.get(
    f"https://www.instagram.com/{username}/",
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

text = response.text

for match in re.finditer(
    "followers",
    text,
    re.IGNORECASE
):
    start = max(0, match.start() - 300)
    end = min(len(text), match.end() + 300)

    print("=" * 80)
    print(text[start:end])
    print("=" * 80)

from app.ingestion.instagram import (
    extract_instagram_metadata
)

data = extract_instagram_metadata(
    "https://www.instagram.com/reel/DKG8krgseWt/"
)

print(data["creator"])
print(data["follower_count"])