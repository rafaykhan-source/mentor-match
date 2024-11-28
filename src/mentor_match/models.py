"""The data models for the application."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Person:
    """A class wrapping information associated with a person."""

    first_name: str
    last_name: str
    email: str
    availability: list[str]

    def __eq__(self, other: object) -> bool:
        """Returns whether the two instances are equal.

        Args:
            other (Self): The other instance.

        Returns:
            bool: Whether the two instances are equal.
        """
        if isinstance(other, Person):
            return self.email == other.email
        return False

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
