from app.vectorstore.vector_store import (
    search_chunks
)

from app.rag.generator import (
    generate_answer
)


def answer_question(
    question
):

    chunks = search_chunks(
        question,
        limit=5
    )

    answer = generate_answer(
        question,
        chunks
    )

    return answer