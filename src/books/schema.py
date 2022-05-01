from src.books.models import Book

from ninja import Schema


class BookOut(Schema):
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
