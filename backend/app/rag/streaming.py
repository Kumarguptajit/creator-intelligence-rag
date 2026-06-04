# backend/app/rag/streaming.py

from app.rag.generator import client


def stream_response(prompt):

    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt
    )

    for chunk in response:

        if chunk.text:
            yield chunk.text