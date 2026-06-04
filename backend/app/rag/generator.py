import os

from dotenv import load_dotenv
from google import genai
from app.rag.memory import (
    format_history
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

    prompt = f"""
    You are a creator intelligence assistant.

    Use the conversation history and retrieved context.

    Conversation History:
    {history}

    Context:
    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text