from embeding_service import create_query_embedding
from vector_store import search_similar_chunks


question = "Which technology can I use for building APIs with Python?"


query_embedding = create_query_embedding(question)


results = search_similar_chunks(
    query_embedding,
    top_k=3
)


print("\nQuestion:")
print(question)


print("\nRetrieved Documents:")

for document in results["documents"][0]:
    print("-", document)