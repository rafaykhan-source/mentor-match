"""The data models for the application."""

from dataclasses import dataclass


@dataclass
class Person:
    """A class wrapping information associated with a person."""

    first_name: str
    last_name: str
    email: str
    availability: list[str]
    meeting_time: str = ""
