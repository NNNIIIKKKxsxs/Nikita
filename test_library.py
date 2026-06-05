import pytest
from library import Library


def test_add_book_success():
    # AAA, EP, positive
    library = Library()

    result = library.add_book("Harry Potter")

    assert result is True
    assert "Harry Potter" in library.books


def test_add_empty_book():
    # AAA, BVA, negative
    library = Library()

    with pytest.raises(ValueError):
        library.add_book("")


def test_add_space_book():
    # AAA, BVA, negative
    library = Library()

    with pytest.raises(ValueError):
        library.add_book("   ")


def test_add_duplicate_book():
    # AAA, EP, negative
    library = Library()
    library.add_book("1984")

    with pytest.raises(ValueError):
        library.add_book("1984")


def test_search_existing_book():
    # AAA, EP, positive
    library = Library()
    library.add_book("Dune")

    result = library.search_book("Dune")

    assert result is True


def test_search_book_case_insensitive():
    # AAA, EP, positive
    library = Library()
    library.add_book("Dune")

    result = library.search_book("dune")

    assert result is True


def test_search_missing_book():
    # AAA, EP, negative
    library = Library()
    library.add_book("Dune")

    result = library.search_book("Metro")

    assert result is False


def test_search_empty_title():
    # AAA, BVA, negative
    library = Library()

    with pytest.raises(ValueError):
        library.search_book("")


def test_borrow_existing_book():
    # AAA, EP, positive
    library = Library()
    library.add_book("Metro 2033")

    result = library.borrow_book("Metro 2033")

    assert result == "Book borrowed"
    assert "Metro 2033" not in library.books


def test_borrow_missing_book():
    # AAA, EP, negative
    library = Library()

    with pytest.raises(ValueError):
        library.borrow_book("Unknown Book")
