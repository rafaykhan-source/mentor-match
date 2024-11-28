"""This module maintains the logic associated with rematch."""

from dataclasses import dataclass

from mentor_match.dataserver import DataServer
from mentor_match.datawriter import DataWriter
from mentor_match.mentee_strategies import SmallestGroupStrategy
from mentor_match.models import Group, Person


def _get_group(mentee: Person, groups: list[Group]) -> Group | None:
    """Returns group associated with mentee.

    Args:
        mentee (Person): The mentee whose group to return.
        groups (list[Group]): The mentorship groups.

    Returns:
        Group | None: The group of the mentee.
    """
    for g in groups:
        if mentee in g.mentees:
            return g
    return None


@dataclass
class RematchEngine:
    """This class is responsible for performing rematches for mentees."""

    rematchees: list[Person]
    "The mentees to rematch."
    groups: list[Group]
    "The existing mentorship groups."

    def _remove_mentee_from_group(self, mentee: Person, group: Group) -> None:
        """Removes mentee from the group.

        Args:
            mentee (Person): The mentee to remove.
            group (Group): The group to remove mentee from.
        """
        group.mentees = [m for m in group.mentees if mentee != m]

    def _prepare_groups(self) -> None:
        """Prepares the groups for reassignment."""
        for m in self.rematchees:
            group = _get_group(m, self.groups)
            if group:
                self._remove_mentee_from_group(m, group)

    def reassign_mentees(self) -> None:
        """Reassigns the mentees."""
        self._prepare_groups()
        s = SmallestGroupStrategy(self.groups, self.rematchees)
        s.assign_mentees()

        writer = DataWriter()
        writer.write_groups(self.groups, "data/placements/groups.json")


@dataclass
class RematchCleaner:
    """This class cleans the data, leaving those who need a rematch."""

    def __post_init__(self) -> None:
        """Retrieves current placements."""
        s = DataServer()
        self.mentees = s.read_people("data/updates/rematchees.json")
        self.groups = s.read_groups("data/placements/groups.json")

    def has_conflict(self, group: Group, mentee: Person) -> bool:
        """Returns whether the mentee has a conflict in a group.

        Args:
            mentee (Person): The mentee with possible conflict.
            group (Group): The group the mentee may have a conflict in.

        Returns:
            bool: Whether the mentee has a conflict.
        """
        return group.meeting_time not in mentee.availability

    def update_rematchees(self) -> None:
        rematchees = []
        for m in self.mentees:
            group = _get_group(m, self.groups)
            if group and (not self.has_conflict(group, m)):
                continue
            rematchees.append(m)

        writer = DataWriter()
        writer.write_people(rematchees, "data/updates/rematchees.json")
