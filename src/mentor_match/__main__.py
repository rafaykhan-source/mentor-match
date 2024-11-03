from mentor_match.dataserver import DataServer
from mentor_match.datawriter import DataWriter
from mentor_match.mentee_strategies import SmallestGroupStrategy
from mentor_match.mentor_strategies import FrequencyStrategy
from mentor_match.models import Group


def main() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")
    groups = [Group(m) for m in mentors]

    p = FrequencyStrategy(groups, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    writer = DataWriter()
    writer.write_entries(groups, "results/groups.csv")


main()
