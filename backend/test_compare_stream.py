from app.ingestion.service import process_youtube_video

from app.rag.comparison import (
    get_video_context,
    build_comparison_prompt
)

from app.rag.streaming import (
    stream_response
)

video_a_url = "https://www.youtube.com/watch?v=4PhVS4VpEbA&pp=ugUHEgVlbi1VUw%3D%3D"
video_b_url = "https://youtu.be/I7_WXKhyGms"

data_a = process_youtube_video(video_a_url)
data_b = process_youtube_video(video_b_url)

context_a = get_video_context(
    "Summarize this video",
    "A"
)

context_b = get_video_context(
    "Summarize this video",
    "B"
)

prompt = build_comparison_prompt(
    data_a["metadata"],
    data_b["metadata"],
    context_a,
    context_b
)

for chunk in stream_response(prompt):

    print(
        chunk,
        end="",
        flush=True
    )