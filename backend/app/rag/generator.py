import os
from dotenv import load_dotenv
from google import genai
from app.rag.memory import (
    format_history
)

from app.rag.comparison_context import (
    get_comparison_context
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(
    question: str,
    retrieved_chunks
):

    context_parts = []

    for chunk in retrieved_chunks:

        context_parts.append(
            f"""
    [{chunk.payload['video_label']} Chunk {chunk.payload['chunk_id']}]

    {chunk.payload['text']}
    """
        )

    context = "\n\n".join(
        context_parts
    )
    history = format_history()
    comparison = get_comparison_context()
    comparison_context = ""

    if comparison:

        comparison_context = f"""
    Video A Metadata:
    {comparison.get("metadata_a")}

    Video B Metadata:
    {comparison.get("metadata_b")}

    Video A Context:
    {comparison.get("context_a")}

    Video B Context:
    {comparison.get("context_b")}
    """

    prompt = f"""
    You are a creator intelligence assistant.

    Use:

    1. Conversation History
    2. Comparison Context
    3. Retrieved Context

    Conversation History:
    {history}

    Comparison Context:
    {comparison_context}

    Retrieved Context:
    {context}

    Question:
    {question}

    IMPORTANT:

    If Comparison Context exists:

    - Assume the user is referring to the current Video A and Video B.
    - Never say you do not have access to the videos.
    - Never ask the user to provide the videos again.
    - Use Comparison Context first.
    - Use Retrieved Context second.
    - Use Conversation History third.

    Support claims using evidence.

    IMPORTANT:

    Every factual claim about a video,
    hook, structure, engagement,
    educational value, strengths,
    weaknesses, or performance MUST
    include a source citation.

    Citation format:

    [Source: A Chunk 1]

    [Source: B Chunk 86]

    Do not make claims without citing
    supporting evidence.

    Use transcript context as the primary source of truth.

    If transcript content conflicts with metadata
    such as title or creator information,
    trust the transcript context.

    For questions about performance,
    consider:

    - Hook
    - Structure
    - Educational value
    - Audience appeal
    - Engagement metrics

    Do not rely only on views, likes, and comments.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text