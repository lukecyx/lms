from typing import TypedDict

from src.helpers.migrations.csv_import import transform


class BookRecord(TypedDict):
    """Represents a record in books.csv."""

    goodreads_book_id: int
    books_count: int
    isbn: str
    isbn13: str
    authors: str
    original_publication_year: int
    original_title: str
    title: str
    language_code: str
    average_rating: float
    ratings_count: int
    image_url: str
    small_image_url: str


csv_row = {
    "book_id": "99",
    "goodreads_book_id": "11857408",
    "best_book_id": "11857408",
    "work_id": "16813814",
    "books_count": "147",
    "isbn": "1612130585",
    "isbn13": "9.78161213058e+12",
    "authors": "E.L. James",
    "original_publication_year": "2011",
    "original_title": "Fifty Shades Darker",
    "title": "Fifty Shades Darker (Fifty Shades, #2)",
    "language_code": "eng",
    "average_rating": "3.87",
    "ratings_count": "552059",
    "work_ratings_count": "623340",
    "work_text_reviews_count": "28052",
    "ratings_1": "37245",
    "ratings_2": "58935",
    "ratings_3": "114203",
    "ratings_4": "150906",
    "ratings_5": "262051",
    "image_url": "https://images.gr-assets.com/books/1358266080m/11857408.jpg",
    "small_image_url": "https://images.gr-assets.com/books/1358266080s/11857408.jpg",
}


def test_csv_transform():
    ret = transform(csv_row, BookRecord)

    for key, value in ret.items():
        assert isinstance(value, BookRecord.__annotations__[key])

    # Make sure that key/value pairs not defined in BookRecord are
    # omitted in the result.
    typed_keys = set(BookRecord.__annotations__.keys())
    csv_row_keys = set(csv_row.keys())
    key_diff = list(typed_keys ^ csv_row_keys)

    for key in key_diff:
        assert key not in set(typed_keys)
