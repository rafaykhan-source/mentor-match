"""This module is responsible for writing data to disk."""

import csv
from abc import ABC, abstractmethod
from dataclasses import dataclass

from mentor_match.models import Group


@dataclass
class FileOutputStrategy(ABC):
    """This interface is for data writing."""

    @abstractmethod
    def write_groups(self, groups: list[Group], file_path: str) -> None:
        """Writes the groups to output.

        Args:
            groups (list[Group]): The groups to write to output.
            file_path (str): The path for the output file.
        """


@dataclass
class CSVOutputStrategy(FileOutputStrategy):
    """This class is for writing data to csv."""

    def write_groups(self, groups: list[Group], file_path: str) -> None:
        """Writes the groups to output.

        Args:
            groups (list[Group]): The groups to write to output.
            file_path (str): The path for the output file.
        """
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
                        "mentor": g.mentor.__repr__(),
                        "mentees": g.mentees,
                        "meeting_time": g.meeting_time,
                    },
                )


class SimpleCSVOutputStrategy(CSVOutputStrategy):
    """This class is for writing data to csv in a simple format."""

    def write_groups(self, groups: list[Group], file_path: str) -> None:
        """Writes the groups to output.

        Args:
            groups (list[Group]): The groups to write to output.
            file_path (str): The path for the output file.
        """
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


@dataclass
class DataWriter:
    """This class is responsible for writing the data."""

    def write_entries(self, groups: list[Group], file_path: str) -> None:
        s = CSVOutputStrategy()
        s.write_groups(groups, file_path)
