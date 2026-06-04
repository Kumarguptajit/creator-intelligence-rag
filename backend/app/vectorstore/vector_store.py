from qdrant_client.models import PointStruct

from app.vectorstore.qdrant_client import client
from app.rag.embeddings import generate_embedding


def store_chunks(embedded_chunks):

    points = []

    for i, chunk in enumerate(embedded_chunks):

        points.append(
            PointStruct(
                id=i,
                vector=chunk["embedding"],
                payload = {
                    "video_label":chunk["video_label"],
                    "video_id": chunk["video_id"],
                    "chunk_id": chunk["chunk_id"],
                    "text": chunk["text"]
                }
            )
        )

    client.upsert(
        collection_name="video_chunks",
        points=points
    )

    print(f"Stored {len(points)} chunks")


def search_chunks(
    query: str,
    limit: int = 5
):

    query_embedding = generate_embedding(
        query
    )

    results = client.query_points(
        collection_name="video_chunks",
        query=query_embedding,
        limit=limit
    )

    return results.points