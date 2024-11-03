from mentor_match.dataserver import DataServer
from mentor_match.mentor_strategies import FrequencyStrategy, RandomStrategy
from mentor_match.models import Group


def test_mentor_time_assignments_not_empty_random() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")
    groups = [Group(m) for m in mentors]

    r = RandomStrategy(groups, mentees)
    r.set_meeting_times()

    for g in groups:
        assert g.meeting_time != ""


def test_mentor_time_assignments_from_availability_random() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")
    groups = [Group(m) for m in mentors]

    r = RandomStrategy(groups, mentees)
    r.set_meeting_times()

    for g in groups:
        assert g.meeting_time in g.mentor.availability


def test_mentor_time_assignments_not_empty_frequency() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")
    groups = [Group(m) for m in mentors]

    r = FrequencyStrategy(groups, mentees)
    r.set_meeting_times()

    for g in groups:
        assert g.meeting_time != ""


def test_mentor_time_assignments_from_availability_frequency() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")
    groups = [Group(m) for m in mentors]

    r = RandomStrategy(groups, mentees)
    r.set_meeting_times()

    for g in groups:
        assert g.meeting_time in g.mentor.availability
