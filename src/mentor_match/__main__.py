from .dataserver import DataServer
from .datawriter import DataWriter
from .mentee_strategies import SmallestGroupStrategy
from .mentor_strategies import FrequencyStrategy


def main() -> None:
    server = DataServer()

    mentors = server.read_entries("data/mentors.csv")
    mentees = server.read_entries("data/mentees.csv")

    p = FrequencyStrategy(mentors, mentees)
    p.set_meeting_times()

    writer = DataWriter()
    writer.write_entries(mentors, "results/mentors.csv")

    r = SmallestGroupStrategy(mentors, mentees)
    r.set_meeting_times()

    writer.write_entries(mentees, "results/mentees.csv")


main()
