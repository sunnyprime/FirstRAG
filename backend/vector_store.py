import chromadb
import uuid


client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="documents"
)


def store_chunks(chunks, embeddings):

    ids = [
    str(uuid.uuid4())
    for _ in chunks
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    return len(chunks)


def search_similar_chunks(query_embedding, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results