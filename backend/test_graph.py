from app.rag.workflow import (
    comparison_graph
)

result = comparison_graph.invoke(
    {
        "prompt": "Explain RAG"
    }
)

print(
    result["answer"]
)