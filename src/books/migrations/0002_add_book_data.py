import csv
import itertools
from typing import TypedDict

from src.helpers.migrations.csv_import import transform

from django.conf import settings
from django.db import migrations


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


def get_csv_rows():
    with open(settings.BASE_DIR / "src/data_files/books.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield transform(row, BookRecord)


def forwards(apps, _):
    Book = apps.get_model("books", "Book")
    book_objs = (Book(**row) for row in get_csv_rows())

    batch_size = 100
    while True:
        batch = list(itertools.islice(book_objs, batch_size))
        if not batch:
            break

        Book.objects.bulk_create(batch, batch_size)


class Migration(migrations.Migration):
    dependencies = [("books", "0001_initial")]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
