from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Embedding model loaded!")


def create_embeddings(chunks):
    return model.encode(chunks).tolist()

def create_query_embedding(query):
    return model.encode(query).tolist()