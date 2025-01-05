"""The strategies responsbile for selecting the mentee meeting times."""

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass

from mentor_match.models import Group, Person


@dataclass
class PlacementStrategy(ABC):
    """Assigns mentees a mentorship group."""

    groups: list[Group]
    mentees: list[Person]

    @abstractmethod
    def assign_mentees(self) -> None:
        """Assigns mentees to mentorship groups."""


@dataclass
class RandomGroupStrategy(PlacementStrategy):
    """Assigns mentees to a random group with their availability."""

    groups: list[Group]
    mentees: list[Person]

    def _get_available_groups(self, mentee: Person) -> list[Group]:
        return [g for g in self.groups if g.meeting_time in mentee.availability]

    def assign_mentees(self) -> None:
        """Assigns mentees to their mentor groups."""
        for m in self.mentees:
            groups = self._get_available_groups(m)
            if not groups:
                continue
            group = random.choice(groups)
            group.mentees.append(m)


@dataclass
class SmallestGroupStrategy(PlacementStrategy):
    """Assigns mentees to a the smallest group with their availability."""

    groups: list[Group]
    mentees: list[Person]

    def _get_smallest_group(self, mentee: Person) -> Group | None:
        size = float("inf")
        smallest = None
        for g in self.groups:
            if g.meeting_time not in mentee.availability:
                continue
            if len(g.mentees) < size:
                smallest = g
                size = len(g.mentees)

        return smallest

    def assign_mentees(self) -> None:
        """Assigns mentees to mentorship groups."""
        for m in self.mentees:
            group = self._get_smallest_group(m)
            if group:
                group.mentees.append(m)
