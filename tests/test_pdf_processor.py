from src.pdf_processor import extract_text_from_pdf


def test_extract_text_from_pdf():
    result = extract_text_from_pdf("data/test.pdf")

    assert isinstance(result, list)
    assert len(result) > 0