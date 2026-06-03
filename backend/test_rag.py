from app.vectorstore.vector_store import search_chunks
from app.rag.generator import generate_answer

question = "What technologies are used to build this AI agent?"

chunks = search_chunks(
    question,
    limit=5
)

answer = generate_answer(
    question,
    chunks
)

print(answer)