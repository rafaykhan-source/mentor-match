"""This module is responsible for writing data to disk."""

import csv
import json
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass

from mentor_match.models import Group, Person


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

    @abstractmethod
    def write_people(self, people: list[Person], file_path: str) -> None:
        """Writes the groups to output.

        Args:
            people (list[Person]): The people to write to output.
            file_path (str): The path for the output file.
        """


@dataclass
class JSONOutputStrategy(FileOutputStrategy):
    """This class is for writing data to json."""

    def write_groups(self, groups: list[Group], file_path: str) -> None:
        """Writes the groups to output.

        Args:
            groups (list[Group]): The groups to write to output.
            file_path (str): The path for the output file.
        """
        with open(file_path, "w") as json_file:
            group_dicts = [asdict(group) for group in groups]
            json.dump(group_dicts, json_file)

    def write_people(self, people: list[Person], file_path: str) -> None:
        """Writes the groups to output.

        Args:
            people (list[Person]): The people to write to output.
            file_path (str): The path for the output file.
        """
        with open(file_path, "w") as json_file:
            people_dicts = [asdict(p) for p in people]
            json.dump(people_dicts, json_file)


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

    def write_people(self, people: list[Person], file_path: str) -> None:
        """Writes the groups to output.

        Args:
            people (list[Person]): The people to write to output.
            file_path (str): The path for the output file.
        """
        with open(file_path, "w", newline="") as csv_file:
            fieldnames = [
                "first_name",
                "last_name",
                "email",
                "availability",
            ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for p in people:
                writer.writerow(
                    {
                        "first_name": p.first_name,
                        "last_name": p.last_name,
                        "email": p.email,
                        "availability": p.availability,
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

    def write_people(self, people: list[Person], file_path: str) -> None:
        """Writes the groups to output.

        Args:
            people (list[Person]): The people to write to output.
            file_path (str): The path for the output file.
        """
        with open(file_path, "w", newline="") as csv_file:
            fieldnames = [
                "first_name",
                "last_name",
            ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for p in people:
                writer.writerow(
                    {
                        "first_name": p.first_name,
                        "last_name": p.last_name,
                    },
                )


@dataclass
class DataWriter:
    """This class is responsible for writing the data."""

    def write_groups(self, groups: list[Group], file_path: str) -> None:
        s = JSONOutputStrategy()
        s.write_groups(groups, file_path)

    def write_people(self, people: list[Person], file_path: str) -> None:
        s = JSONOutputStrategy()
        s.write_people(people, file_path)
