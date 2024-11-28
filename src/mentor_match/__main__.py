from mentor_match.dataserver import DataServer
from mentor_match.mentee_strategies import SmallestGroupStrategy
from mentor_match.mentor_strategies import FrequencyStrategy
from mentor_match.models import Group
from mentor_match.rematch import RematchCleaner, RematchEngine


def initial_match() -> None:
    server = DataServer()
    mentors = server.read_people("data/original/mentors.json")
    mentees = server.read_people("data/original/mentees.json")
    groups = [Group(m) for m in mentors]

    p = FrequencyStrategy(groups, mentees)
    p.set_meeting_times()

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    print("\n".join([str(len(g.mentees)) for g in groups]))


def _clean() -> None:
    c = RematchCleaner()
    c.update_rematchees()


def rematch() -> None:
    _clean()

    s = DataServer()
    rematchees = s.read_people("data/updates/rematchees.json")
    groups = s.read_groups("data/placements/groups.json")

    r = RematchEngine(rematchees, groups)
    r.reassign_mentees()


def main() -> None:
    initial_match()


main()
