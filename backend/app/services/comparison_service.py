from app.ingestion.service import (
    process_video
)
from app.rag.comparison_context import (
    save_comparison_context
)

from app.rag.comparison import (
    get_video_context,
    build_comparison_prompt
)

from app.rag.workflow import (
    comparison_graph
)




def prepare_comparison(
    video_a_url,
    video_b_url
):

    data_a = process_video(
        video_a_url
    )

    data_b = process_video(
        video_b_url
    )

    context_a = get_video_context(
        "Summarize this video",
        "A"
    )

    context_b = get_video_context(
        "Summarize this video",
        "B"
    )

    save_comparison_context(
        data_a["metadata"],
        data_b["metadata"],
        context_a,
        context_b
    )

    prompt = build_comparison_prompt(
        data_a["metadata"],
        data_b["metadata"],
        context_a,
        context_b
    )

    result = comparison_graph.invoke(
        {
            "prompt": prompt
        }
    )

    return result["answer"]