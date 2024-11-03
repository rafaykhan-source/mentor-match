"""This module is responsible for writing data to disk."""

import csv
from dataclasses import dataclass

from mentor_match.models import Group


@dataclass
class DataWriter:
    """This class is responsible for writing the data."""

    def write_entries(self, groups: list[Group], file_path: str) -> None:
        with open(file_path, "w", newline="") as csv_file:
            fieldnames = [
                "mentor",
                "mentees",
                "meeting_time",
            ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for g in groups:
                writer.writerow(
                    {
                        "mentor": str(g.mentor),
                        "mentees": ", ".join([str(m) for m in g.mentees]),
                        "meeting_time": g.meeting_time,
                    },
                )
