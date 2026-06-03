from app.vectorstore.vector_store import search_chunks

results = search_chunks(
    "What is this AI agent about?"
)

for result in results:

    print()
    print("Video:", result.payload["video_id"])
    print("Chunk:", result.payload["chunk_id"])
    print()
    print(result.payload["text"][:300])