"""The strategies responsbile for selecting the mentee meeting times."""

from dataclasses import dataclass

from .models import Person


@dataclass
class SmallestGroupStrategy:
    """Selects meeting times for mentees based on smallest available group."""

    mentors: list[Person]
    mentees: list[Person]

    def __post_init__(self) -> None:
        """Instantiates fields related to the strategy."""
        self.meeting_times = {m.meeting_time: 0 for m in self.mentors}

    def _get_smallest_group(self, mentee: Person) -> str:
        smallest = ""
        for t in self.meeting_times:
            if t not in mentee.availability:
                continue
            if smallest == "" or (self.meeting_times[t] < self.meeting_times[smallest]):
                smallest = t

        return smallest

    def set_meeting_times(self) -> None:
        """Sets the meeting times for the mentees."""
        for m in self.mentees:
            smallest = self._get_smallest_group(m)
            print(smallest)
            if smallest:
                self.meeting_times[smallest] += 1
                m.meeting_time = smallest
