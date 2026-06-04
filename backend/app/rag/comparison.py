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

1. Why Video A may outperform Video B
2. Differences in content approach
3. Differences in hook quality
4. Suggestions for improving Video B

Use evidence from the transcript context.
"""