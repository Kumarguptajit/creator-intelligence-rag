from app.rag.chunker import chunk_text
from app.ingestion.service import process_youtube_video
from app.rag.embeddings import embed_chunks
from app.vectorstore.vector_store import search_chunks
from app.vectorstore.vector_store import (
    search_chunks,
    store_chunks
)



video_a_url = "https://www.youtube.com/watch?v=4PhVS4VpEbA&pp=ugUHEgVlbi1VUw%3D%3D"
video_b_url="https://youtu.be/I7_WXKhyGms"

data_a = process_youtube_video(
    video_a_url
)

chunks_a = chunk_text(
    data_a["transcript"],
    data_a["metadata"]["video_id"],
    "A"
)

data_b = process_youtube_video(
    video_b_url
)

chunks_b = chunk_text(
    data_b["transcript"],
    data_b["metadata"]["video_id"],
    "B"
)

all_chunks = chunks_a + chunks_b
embedded_chunks = embed_chunks(
    all_chunks
)
store_chunks(
    embedded_chunks
)

print(
    len(chunks_a),
    len(chunks_b)
)

print(
    len(embedded_chunks)
)

results = search_chunks(
    "What technologies are used?",
    limit = 20
)

for result in results:

    print(
        result.payload["video_label"],
        result.payload["chunk_id"]
    )