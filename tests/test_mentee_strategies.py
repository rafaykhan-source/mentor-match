from mentor_match.dataserver import DataServer
from mentor_match.mentee_strategies import SmallestGroupStrategy
from mentor_match.mentor_strategies import FrequencyStrategy, RandomStrategy
from mentor_match.models import Group


def test_mentee_time_assignments_not_empty_random() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")
    groups = [Group(m) for m in mentors]

    p = RandomStrategy(groups, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        assert g.meeting_time != ""


def test_mentee_time_assignments_from_availability_random() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")
    groups = [Group(m) for m in mentors]

    p = RandomStrategy(groups, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        for m in g.mentees:
            assert g.meeting_time in m.availability


def test_mentee_time_assignments_not_empty_frequency() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")
    groups = [Group(m) for m in mentors]

    p = FrequencyStrategy(groups, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        assert g.meeting_time != ""


def test_mentee_time_assignments_from_availability_frequency() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")
    groups = [Group(m) for m in mentors]

    p = FrequencyStrategy(groups, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        for m in g.mentees:
            assert g.meeting_time in m.availability
