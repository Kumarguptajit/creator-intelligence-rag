from app.vectorstore.vector_store import search_video_chunks

from app.rag.gemini_client import generate_content

from app.rag.memory import format_history


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

    context_parts = []
    for result in results:
        context_parts.append(
                    f"""
        [{result.payload['video_label']} | Chunk {result.payload['chunk_id']}]

        {result.payload['text']}
                    """
                            )
    context = "\n\n".join(context_parts)
    return context



def build_comparison_prompt(
    metadata_a,
    metadata_b,
    context_a,
    context_b
):
    history = format_history()

    return f"""
You are a creator intelligence analyst.

Conversation History:
{history}

Video A Metadata:
{metadata_a}

Video B Metadata:
{metadata_b}

Video A Transcript Context:
{context_a}

Video B Transcript Context:
{context_b}

Analyze the two videos as a creator intelligence analyst.

Tasks:

1. Compare engagement rates and explain what they indicate.
2. Compare the opening hook and first-impression effectiveness.
3. Compare content structure and pacing.
4. Compare educational value and practical usefulness.
5. Identify strengths of Video A.
6. Identify strengths of Video B.
7. Explain why one video may outperform the other.
8. Suggest 3 specific improvements for Video B.
9. Support every major claim with transcript evidence.

IMPORTANT:

When making a claim, cite the source.

Example:

Video A demonstrates the final application early in the video.
[Source: A Chunk 51]

Video B begins with conceptual explanations before practical examples.
[Source: B Chunk 99]

Output Format:

## Engagement Analysis

## Hook Comparison

## Content Structure

## Educational Value

## Why One Video May Outperform The Other

## Improvements For Video B
"""


def compare_videos(prompt):

    response = generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text