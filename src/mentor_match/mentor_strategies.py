"""The strategies responsible for selecting a weekly meeting time for mentors."""

import random
from collections import Counter
from dataclasses import dataclass

from mentor_match.models import Group, Person


@dataclass
class RandomStrategy:
    """Selects weekly meeting times for mentors randomly from their availability."""

    groups: list[Group]
    mentees: list[Person]

    def set_meeting_times(self) -> None:
        """Sets the meeting times for the set of mentors."""
        for g in self.groups:
            g.meeting_time = random.choice(g.mentor.availability)


@dataclass
class FrequencyStrategy:
    """Selects weekly meeting times for mentors based on availability frequency."""

    groups: list[Group]
    mentees: list[Person]

    def _get_time_frequencies(self) -> Counter[str]:
        frequencies: Counter[str] = Counter()
        for m in self.mentees:
            frequencies.update(m.availability)

        return frequencies

    def set_meeting_times(self) -> None:
        """Sets the meeting times for the mentors."""
        frequencies = self._get_time_frequencies().most_common()
        overlaps = set()

        for g in self.groups:
            for time, _ in frequencies:
                if time in overlaps:
                    continue
                if time in g.mentor.availability:
                    g.meeting_time = time
                    overlaps.add(time)
                    break

        # Permit Overlaps for Remaining Mentors
        for g in self.groups:
            if g.meeting_time:
                continue

            for time, _ in frequencies:
                if time in g.mentor.availability:
                    g.meeting_time = time
