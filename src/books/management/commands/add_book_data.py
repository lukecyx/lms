import itertools
from typing import TypedDict

from src.books.management.commands._private import SharedBookCommand
from src.books.models import Book
from src.helpers.commands.csv_import import transform


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


class Command(SharedBookCommand):
    help = "Add books data from src/data_files/books.csv"
    filenpath = "src/data_files/books.csv"

    def handle(self, *args, **kwargs):
        book_objs = (
            Book(**transform(row, BookRecord))
            for row in self.yield_csv_rows(self.filenpath)
        )

        batch_size = 100
        book_count = 0
        while True:
            batch = list(itertools.islice(book_objs, batch_size))
            book_count += len(batch)

            if not batch:
                break

            Book.objects.bulk_create(batch, batch_size)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully imported {book_count} books")
        )
