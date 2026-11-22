import re


def clean_text(text):
    if not text:
        return ""

    # Remove null characters
    text = text.replace("\x00", "")

    # Replace multiple spaces with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace multiple newlines with a single newline
    text = re.sub(r"\n+", "\n", text)

    # Remove spaces at the beginning and end
    text = text.strip()

    return text
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
