from mentor_match.dataserver import DataServer
from mentor_match.mentee_strategies import SmallestGroupStrategy
from mentor_match.mentor_strategies import FrequencyStrategy, RandomStrategy


def test_mentee_time_assignments_not_empty_random() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")

    p = RandomStrategy(mentors, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(mentors, mentees)
    r.set_meeting_times()

    for m in mentees:
        assert m.meeting_time != ""


def test_mentee_time_assignments_from_availability_random() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")

    p = RandomStrategy(mentors, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(mentors, mentees)
    r.set_meeting_times()

    for m in mentees:
        assert m.meeting_time in m.availability


def test_mentee_time_assignments_not_empty_frequency() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")

    p = FrequencyStrategy(mentors, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(mentors, mentees)
    r.set_meeting_times()

    for m in mentees:
        assert m.meeting_time != ""


def test_mentee_time_assignments_from_availability_frequency() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")

    p = FrequencyStrategy(mentors, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(mentors, mentees)
    r.set_meeting_times()

    for m in mentees:
        assert m.meeting_time in m.availability
