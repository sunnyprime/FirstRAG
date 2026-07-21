from embeding_service import create_embeddings
from vector_store import store_chunks


chunks = [
    "React is a JavaScript library for building user interfaces.",
    "FastAPI is a Python framework for creating APIs.",
    "RAG combines retrieval with language model generation."
]


embeddings = create_embeddings(chunks)


total = store_chunks(
    chunks,
    embeddings
)


print("Stored chunks:", total)