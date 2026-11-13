import fitz


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """
    document = fitz.open(pdf_path)

    extracted_pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text()

        extracted_pages.append({
            "page": page_number,
            "text": text
        })

    document.close()

    return extracted_pages
def get_full_text(pdf_path):
    pages = extract_text_from_pdf(pdf_path)

    full_text = ""

    for page in pages:
        full_text += page["text"] + "\n"

    return full_text