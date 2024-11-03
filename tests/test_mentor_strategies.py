from mentor_match.dataserver import DataServer
from mentor_match.mentor_strategies import FrequencyStrategy, RandomStrategy


def test_mentor_time_assignments_not_empty_random() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")

    r = RandomStrategy(mentors, mentees)
    r.set_meeting_times()

    for m in mentors:
        assert m.meeting_time != ""


def test_mentor_time_assignments_from_availability_random() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")

    r = RandomStrategy(mentors, mentees)
    r.set_meeting_times()

    for m in mentors:
        assert m.meeting_time in m.availability


def test_mentor_time_assignments_not_empty_frequency() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")

    r = FrequencyStrategy(mentors, mentees)
    r.set_meeting_times()

    for m in mentors:
        assert m.meeting_time != ""


def test_mentor_time_assignments_from_availability_frequency() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")

    r = RandomStrategy(mentors, mentees)
    r.set_meeting_times()

    for m in mentors:
        assert m.meeting_time in m.availability
