import os

from app.routes import comparison
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

    context = "\n\n".join(
        [
            chunk.payload["text"]
            for chunk in retrieved_chunks
        ]
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

    If the user asks follow-up questions
    about Video A, Video B, hooks,
    engagement, educational value,
    improvements, or comparison results,
    use the comparison context first.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text