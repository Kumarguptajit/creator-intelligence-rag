from app.rag.streaming import stream_response

prompt = """
Explain Retrieval Augmented Generation in simple terms.
"""

for chunk in stream_response(prompt):

    print(
        chunk,
        end="",
        flush=True
    )