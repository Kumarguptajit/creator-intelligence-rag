from app.vectorstore.vector_store import (
    search_chunks
)

from app.rag.generator import (
    generate_answer
)

from app.rag.memory import (
    add_message
)


def answer_question(
    question
):

    add_message(
        "user",
        question
    )

    chunks = search_chunks(
        question,
        limit=5
    )

    answer = generate_answer(
        question,
        chunks
    )

    add_message(
        "assistant",
        answer
    )

    return answer