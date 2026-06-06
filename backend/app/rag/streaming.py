# backend/app/rag/streaming.py

from app.rag.gemini_client import generate_content_stream


def stream_response(prompt):

    response = generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt
    )

    for chunk in response:

        if chunk.text:
            yield chunk.text