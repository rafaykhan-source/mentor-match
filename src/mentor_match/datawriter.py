"""This module is responsible for writing data to disk."""

import csv
from dataclasses import asdict, dataclass

from .models import Person


@dataclass
class DataWriter:
    """This class is responsible for writing the data."""

    def write_entries(self, people: list[Person], file_path: str) -> None:
        with open(file_path, "w", newline="") as csvfile:
            fieldnames = [
                "first_name",
                "last_name",
                "email",
                "availability",
                "meeting_time",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for p in people:
                writer.writerow(asdict(p))
