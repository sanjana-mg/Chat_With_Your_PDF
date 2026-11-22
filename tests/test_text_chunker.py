from src.text_chunker import split_text_into_chunks, clean_text


def test_split_text_into_chunks():
    text = "ABCDEFGHIJ"

    result = split_text_into_chunks(
        text,
        chunk_size=4,
        overlap=1
    )

    assert result == ["ABCD", "DEFG", "GHIJ"]
def test_empty_text():
    result = split_text_into_chunks(
        "",
        chunk_size=4,
        overlap=1
    )

    assert result == []

def test_short_text():
    result = split_text_into_chunks(
        "ABC",
        chunk_size=4,
        overlap=1
    )

    assert result == ["ABC"]

def test_invalid_chunk_size():
    try:
        split_text_into_chunks(
            "ABCDEFGHIJ",
            chunk_size=0,
            overlap=1
        )
        assert False, "Expected ValueError"
    except ValueError:
        assert True

def test_invalid_overlap():
    try:
        split_text_into_chunks(
            "ABCDEFGHIJ",
            chunk_size=4,
            overlap=4
        )
        assert False, "Expected ValueError"
    except ValueError:
        assert True

def test_long_text():
    text = "ABCDEFGHIJKL"

    result = split_text_into_chunks(
        text,
        chunk_size=4,
        overlap=1
    )

    assert result == ["ABCD", "DEFG", "GHIJ", "JKL"]

def test_exact_chunk_size():
    text = "ABCDEFGH"

    result = split_text_into_chunks(
        text,
        chunk_size=4,
        overlap=1
    )

    assert result == ["ABCD", "DEFG", "GH"]
def test_clean_text():
    text = "  Hello    world!\n\nPython\tprogramming  "
    result = clean_text(text)

    assert result == "Hello world!\nPython programming"

