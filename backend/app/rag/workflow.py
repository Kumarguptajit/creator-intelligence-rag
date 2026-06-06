from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import END
from app.rag.comparison import compare_videos


class ComparisonState(TypedDict):

    video_a_url: str

    video_b_url: str

    prompt: str

    answer: str




def generate_node(state):

    answer = compare_videos(
        state["prompt"]
    )

    return {
        "answer": answer
    }

graph = StateGraph(
    ComparisonState
)

graph.add_node(
    "generate",
    generate_node
)

graph.set_entry_point(
    "generate"
)

graph.add_edge(
    "generate",
    END
)

comparison_graph = graph.compile()