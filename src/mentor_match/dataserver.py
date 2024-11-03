"""This module is responsible for reading data for the mentor match program."""

import ast
import csv
from dataclasses import dataclass

from mentor_match.models import Person


@dataclass
class DataServer:
    """This class is responsible for serving the data."""

    def read_entries(self, file_path: str) -> list[Person]:
        with open(file_path) as f:
            reader = csv.DictReader(f)
            return [
                Person(
                    row["first_name"],
                    row["last_name"],
                    row["email"],
                    ast.literal_eval(row["availability"]),
                )
                for row in reader
            ]
