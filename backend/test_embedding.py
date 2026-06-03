from app.rag.embeddings import generate_embedding

embedding = generate_embedding(
    "This is a test sentence."
)

print(type(embedding))
print(len(embedding))
print(embedding[:5])