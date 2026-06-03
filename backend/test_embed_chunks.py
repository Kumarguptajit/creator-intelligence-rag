from app.ingestion.service import process_youtube_video
from app.rag.chunker import chunk_text
from app.rag.embeddings import embed_chunks

url = "https://www.youtube.com/watch?v=4PhVS4VpEbA&pp=ugUHEgVlbi1VUw%3D%3D"

data = process_youtube_video(url)

chunks = chunk_text(
    data["transcript"],
    data["metadata"]["video_id"]
)

embedded_chunks = embed_chunks(chunks)

print(len(embedded_chunks))

print(
    len(
        embedded_chunks[0]["embedding"]
    )
)

print(
    embedded_chunks[0]["video_id"]
)