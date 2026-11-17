def split_text_into_chunks(text, chunk_size=100, overlap=20):
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Invalid overlap value")
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        if end >= len(text):
            break
        start = end - overlap

    return chunks
