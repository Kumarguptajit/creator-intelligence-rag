# test_store_chunks.py

from app.ingestion.service import process_youtube_video
from app.rag.chunker import chunk_text
from app.rag.embeddings import embed_chunks

from app.vectorstore.vector_store import store_chunks

url = "https://www.youtube.com/watch?v=4PhVS4VpEbA&pp=ugUHEgVlbi1VUw%3D%3D"

data = process_youtube_video(url)

chunks = chunk_text(
    data["transcript"],
    data["metadata"]["video_id"]
)

embedded_chunks = embed_chunks(chunks)

store_chunks(embedded_chunks)