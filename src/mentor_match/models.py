"""The data models for the application."""

from dataclasses import dataclass, field


@dataclass
class Person:
    """A class wrapping information associated with a person."""

    first_name: str
    last_name: str
    email: str
    availability: list[str]

    def __str__(self) -> str:
        """Returns a human readable string representation of the object.

        Returns:
            str: A human readable string representation of the object.
        """
        return f"{self.first_name} {self.last_name}"


@dataclass
class Group:
    """A class wrapping the information associated with a mentorship group."""

    mentor: Person
    meeting_time: str = ""
    mentees: list[Person] = field(default_factory=list)
