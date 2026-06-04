
from app.vectorstore.vector_store import search_video_chunks


results_a = search_video_chunks(
    "What is discussed?",
    "A"
)

results_b = search_video_chunks(
    "What is discussed?",
    "B"
)

print("A:", len(results_a))
print("B:", len(results_b))