import os
from src.pdf_processor import get_full_text
from src.text_chunker import split_text_into_chunks, clean_text
def process_document(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError("PDF file not found")
    text = get_full_text(pdf_path)
    text = clean_text(text)

    chunks = split_text_into_chunks(
        text,
        chunk_size=500,
        overlap=50
    )

    return chunks  