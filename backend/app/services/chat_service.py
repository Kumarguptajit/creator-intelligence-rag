from app.vectorstore.vector_store import (
    search_chunks
)

from app.rag.generator import (
    generate_answer
)

from app.rag.memory import (
    add_message
)

from app.rag.comparison_context import (
    get_comparison_context
)

def answer_question(
    question
):

    add_message(
        "user",
        question
    )

    comparison = get_comparison_context()
    print(comparison.keys())
    
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