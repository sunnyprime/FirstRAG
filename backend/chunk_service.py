def split_text(text, chunk_size=500, overlap=100):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# if __name__ == "__main__":
#     sample = (
#         "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         * 40
#     )

#     chunks = split_text(sample)

#     print("Total Chunks:", len(chunks))

#     for i, chunk in enumerate(chunks):
#         print(f"\nChunk {i+1}")
#         print(chunk[:60])