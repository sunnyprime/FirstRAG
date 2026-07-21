from rag_service import ask_question


question = "Which technology can I use for building APIs with Python?"

result = ask_question(question)


print("\nQuestion:")
print(question)


print("\nRetrieved Context:")

for document in result["context"]:
    print("-", document)


print("\nLLM Answer:")
print(result["answer"])