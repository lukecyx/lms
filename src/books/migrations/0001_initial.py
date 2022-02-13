# Generated by Django 4.0.2 on 2022-02-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("goodreads_book_id", models.IntegerField()),
                ("books_count", models.IntegerField()),
                ("isbn", models.CharField(max_length=255)),
                ("isbn13", models.CharField(max_length=255)),
                ("authors", models.CharField(max_length=255)),
                ("original_publication_year", models.IntegerField()),
                ("original_title", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("language_code", models.CharField(max_length=255)),
                ("average_rating", models.FloatField()),
                ("ratings_count", models.IntegerField()),
                ("image_url", models.CharField(max_length=255)),
                ("small_image_url", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
