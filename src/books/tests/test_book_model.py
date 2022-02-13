import datetime

from src.books.models import Book

import pytest
from freezegun import freeze_time


@freeze_time("2022-02-13 12:00:00")
class TestBookModel:
    @pytest.mark.django_db
    def test_create_book(self):
        book = Book.objects.create(
            goodreads_book_id=1337,
            books_count=4,
            isbn="123456789",
            isbn13="123456789 123",
            authors="Stephen King",
            original_publication_year=1986,
            original_title="It",
            title="It",
            language_code="eng",
            average_rating=4.5,
            ratings_count=100,
            image_url="clown-image.com",
            small_image_url="small-clown-image.com",
        )

        assert Book.objects.filter(pk=1).exists() is True

        assert book.created_at == datetime.datetime(
            2022, 2, 13, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        assert book.modified_at == datetime.datetime(
            2022, 2, 13, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        assert book.goodreads_book_id == 1337
        assert book.books_count == 4
        assert book.isbn == "123456789"
        assert book.isbn13 == "123456789 123"
        assert book.authors == "Stephen King"
        assert book.original_publication_year == 1986
        assert book.original_title == "It"
        assert book.language_code == "eng"
        assert book.average_rating == 4.5
        assert book.ratings_count == 100
        assert book.image_url == "clown-image.com"
        assert book.small_image_url == "small-clown-image.com"

        assert str(book) == f"Book(title={book.title} isbn={book.isbn})"
        assert repr(book) == f"<Book: Book(title={book.title} isbn={book.isbn})>"
