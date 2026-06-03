from app.ingestion.service import process_youtube_video
from app.rag.chunker import chunk_text

url = "https://www.youtube.com/watch?v=4PhVS4VpEbA&pp=ugUHEgVlbi1VUw%3D%3D"

data = process_youtube_video(url)

chunks = chunk_text(
    data["transcript"]
)

print("Chunk count:", len(chunks))

print()

print(chunks[0])