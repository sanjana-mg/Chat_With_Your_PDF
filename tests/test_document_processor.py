import pytest 
from src.document_processor import process_document


def test_process_document():
    result = process_document("data/sample.pdf")

    assert isinstance(result, list)
    assert len(result) > 0

def test_invalid_pdf_path():
    with pytest.raises(FileNotFoundError):
        process_document("data/wrong.pdf")