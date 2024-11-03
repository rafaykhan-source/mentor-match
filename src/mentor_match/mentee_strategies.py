"""The strategies responsbile for selecting the mentee meeting times."""

from dataclasses import dataclass

from mentor_match.models import Group, Person


@dataclass
class SmallestGroupStrategy:
    """Selects meeting times for mentees based on smallest available group."""

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
        """Assigns mentees to their mentor groups."""
        for m in self.mentees:
            group = self._get_smallest_group(m)
            if group:
                group.mentees.append(m)
