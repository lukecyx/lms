import csv
import pathlib
from typing import Iterator

from django.core.management.base import BaseCommand, CommandError


class SharedBookCommand(BaseCommand):
    def yield_csv_rows(self, filepath: str) -> Iterator[dict]:
        """Iterator that yields each csv row in a csv file.

        :param filepath: Csv file to open.
        :yields: Iterator of dicts.
        """

        if not pathlib.Path(filepath).is_file():
            raise CommandError(f"File::{filepath} not found")

        with open(filepath, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                yield row
