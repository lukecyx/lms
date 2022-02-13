from src.core.models import TimestampedModel

from django.db import models


class Book(TimestampedModel):
    goodreads_book_id = models.IntegerField()
    books_count = models.IntegerField()
    isbn = models.CharField(max_length=255)
    isbn13 = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    original_publication_year = models.IntegerField()
    original_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    language_code = models.CharField(max_length=255)
    average_rating = models.FloatField()
    ratings_count = models.IntegerField()
    image_url = models.CharField(max_length=255)
    small_image_url = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Book(title={self.title} isbn={self.isbn})"
