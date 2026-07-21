from embeding_service import create_query_embedding
from vector_store import search_similar_chunks
from llm import generate_answer


def ask_question(question: str):

    # 1. Convert question into embedding
    query_embedding = create_query_embedding(question)

    # 2. Search relevant chunks
    results = search_similar_chunks(
        query_embedding,
        top_k=3
    )

    # 3. Get retrieved text
    documents = results["documents"][0]

    # 4. Combine chunks into one context
    context = "\n\n".join(documents)

    # 5. Send question + context to LLM
    answer = generate_answer(
        question=question,
        context=context
    )

    return {
        "answer": answer,
        "context": documents
    }