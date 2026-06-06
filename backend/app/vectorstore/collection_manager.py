from qdrant_client.models import Distance
from qdrant_client.models import VectorParams
from qdrant_client.http import models

from app.vectorstore.qdrant_client import client


def create_collection():

    client.recreate_collection(
        collection_name="video_chunks",
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    client.create_payload_index(
        collection_name="video_chunks",
        field_name="video_label",
        field_schema=models.PayloadSchemaType.KEYWORD
    )

    print("Collection created")