from qdrant_client.models import Distance
from qdrant_client.models import VectorParams

from app.vectorstore.qdrant_client import client


def create_collection():

    client.recreate_collection(
        collection_name="video_chunks",
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    print("Collection created")