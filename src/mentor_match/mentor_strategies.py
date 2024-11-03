"""The strategies responsible for selecting a weekly meeting time for mentors."""

import random
from collections import Counter
from dataclasses import dataclass

from .models import Person


@dataclass
class RandomStrategy:
    """Selects weekly meeting times for mentors randomly from their availability."""

    mentors: list[Person]
    mentees: list[Person]

    def set_meeting_times(self) -> None:
        """Sets the meeting times for the set of mentors."""
        for m in self.mentors:
            m.meeting_time = random.choice(m.availability)


@dataclass
class FrequencyStrategy:
    """Selects weekly meeting times for mentors based on availability frequency."""

    mentors: list[Person]
    mentees: list[Person]

    def _get_time_frequencies(self) -> Counter:
        frequencies: Counter = Counter()
        for m in self.mentees:
            frequencies.update(m.availability)
        for m in self.mentors:
            frequencies.update(m.availability)

        return frequencies

    def set_meeting_times(self) -> None:
        """Sets the meeting times for the set of mentors."""
        frequencies = self._get_time_frequencies().most_common()
        overlaps = set()

        for m in self.mentors:
            for time, _ in frequencies:
                if time in overlaps:
                    continue
                if time in m.availability:
                    m.meeting_time = time
                    overlaps.add(time)
                    break

        # Permit Overlaps for Remaining Mentors
        for m in self.mentors:
            if m.meeting_time:
                continue

            for time, _ in frequencies:
                if time in m.availability:
                    m.meeting_time = time
