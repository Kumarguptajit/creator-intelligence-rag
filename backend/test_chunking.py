from app.ingestion.service import process_youtube_video
from app.rag.chunker import chunk_text
from app.ingestion.transcript import get_video_id

url = "https://www.youtube.com/watch?v=4PhVS4VpEbA&pp=ugUHEgVlbi1VUw%3D%3D"

data = process_youtube_video(url)


chunks = chunk_text(
    data["transcript"],
    get_video_id(url)
)

print("Chunk count:", len(chunks))


print(chunks[0])