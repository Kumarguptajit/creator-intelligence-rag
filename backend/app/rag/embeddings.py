from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

def generate_embedding(text: str):

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()


def embed_chunks(chunks):

    embedded_chunks = []

    for chunk in chunks:

        embedding = generate_embedding(
            chunk["text"]
        )

        embedded_chunks.append(
            {
                **chunk,
                "embedding": embedding
            }
        )

    return embedded_chunks