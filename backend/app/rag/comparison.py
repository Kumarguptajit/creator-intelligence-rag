from app.vectorstore.vector_store import search_video_chunks

from app.rag.generator import client


def get_video_context(
    query,
    video_label
):

    results = search_video_chunks(
        query=query,
        video_label=video_label,
        limit=5
    )

    context = "\n\n".join(
        [
            result.payload["text"]
            for result in results
        ]
    )

    return context



def build_comparison_prompt(
    metadata_a,
    metadata_b,
    context_a,
    context_b
):

    return f"""
You are a creator intelligence analyst.

Video A Metadata:
{metadata_a}

Video B Metadata:
{metadata_b}

Video A Transcript Context:
{context_a}

Video B Transcript Context:
{context_b}

Analyze:

1. Compare engagement rates.
2. Compare content structure.
3. Compare educational value.
4. Compare likely hook effectiveness.
5. Explain why one video may outperform the other.
6. Suggest improvements for Video B.
7. Cite evidence from the transcript context.

Use evidence from the transcript context.
"""


def compare_videos(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text