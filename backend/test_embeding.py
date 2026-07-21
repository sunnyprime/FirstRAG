from embeding_service import create_embeddings

chunks = [
    "I love React.",
    "I know Python.",
    "I enjoy cooking."
]

embeddings = create_embeddings(chunks)

print("Total embeddings:", len(embeddings))
print("Dimensions:", len(embeddings[0]))
print("First 10 values:")
print(embeddings[0][:10])