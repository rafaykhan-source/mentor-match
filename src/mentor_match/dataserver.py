"""This module is responsible for reading data for the mentor match program."""

import ast
import csv
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass

from mentor_match.models import Group, Person


@dataclass
class FileInputStrategy(ABC):
    """This interface is for data reading."""

    @abstractmethod
    def read_people(self, file_path: str) -> list[Person]:
        """Returns the list of people at file_path.

        Args:
            file_path (str): The file path of the people.

        Returns:
            list[Person]: The people.
        """

    @abstractmethod
    def read_groups(self, file_path: str) -> list[Group]:
        """Returns the list of groups at file_path.

        Args:
            file_path (str): The file path of the groups.

        Returns:
            list[Group]: The groups.
        """


@dataclass
class CSVInputStrategy(FileInputStrategy):
    """This class is for reading data from csv."""

    def read_people(self, file_path: str) -> list[Person]:
        """Returns the list of people at file_path.

        Args:
            file_path (str): The file path of the people.

        Returns:
            list[Person]: The people.
        """
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            return [
                Person(
                    r["first_name"],
                    r["last_name"],
                    r["email"],
                    ast.literal_eval(r["availability"]),
                )
                for r in reader
            ]

    def read_groups(self, file_path: str) -> list[Group]:
        """Returns the list of groups at file_path.

        Args:
            file_path (str): The file path of the groups.

        Returns:
            list[Group]: The groups.
        """
        del file_path
        return []


@dataclass
class JSONInputStrategy(FileInputStrategy):
    """This class is for reading data from json."""

    def read_people(self, file_path: str) -> list[Person]:
        """Returns the list of people at file_path.

        Args:
            file_path (str): The file path of the people.

        Returns:
            list[Person]: The people.
        """
        with open(file_path) as json_file:
            raw_people = json.load(json_file)
            return [
                Person(p["first_name"], p["last_name"], p["email"], p["availability"])
                for p in raw_people
            ]

    def read_groups(self, file_path: str) -> list[Group]:
        """Returns the list of groups at file_path.

        Args:
            file_path (str): The file path of the groups.

        Returns:
            list[Group]: The groups.
        """
        with open(file_path) as json_file:
            raw_groups = json.load(json_file)
            groups = []
            for g in raw_groups:
                mentor = Person(
                    g["mentor"]["first_name"],
                    g["mentor"]["last_name"],
                    g["mentor"]["email"],
                    g["mentor"]["availability"],
                )
                mentees = [
                    Person(
                        m["first_name"],
                        m["last_name"],
                        m["email"],
                        m["availability"],
                    )
                    for m in g["mentees"]
                ]

                groups.append(Group(mentor, g["meeting_time"], mentees))

            return groups


@dataclass
class DataServer:
    """This class is responsible for serving the data."""

    def read_people(self, file_path: str) -> list[Person]:
        """Returns the list of people at file_path.

        Args:
            file_path (str): The file path of the people.

        Returns:
            list[Person]: The people.
        """
        s = JSONInputStrategy()
        return s.read_people(file_path)

    def read_groups(self, file_path: str) -> list[Group]:
        """Returns the list of groups at file_path.

        Args:
            file_path (str): The file path of the groups.

        Returns:
            list[Group]: The groups.
        """
        s = JSONInputStrategy()
        return s.read_groups(file_path)
