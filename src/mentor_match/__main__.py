import argparse

from mentor_match.dataserver import DataServer
from mentor_match.mentee_strategies import SmallestGroupStrategy
from mentor_match.mentor_strategies import FrequencyStrategy
from mentor_match.models import Group
from mentor_match.rematch import RematchCleaner, RematchEngine


def get_args() -> argparse.Namespace:
    """Returns program arguments."""
    parser = argparse.ArgumentParser(
        prog="mentor-match",
        description="Forms mentorship groups between students and mentors.",
    )
    parser.add_argument("operation", help="match, rematch, or clean")
    return parser.parse_args()


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


def clean() -> None:
    c = RematchCleaner()
    c.update_rematchees()


def rematch() -> None:
    clean()

    s = DataServer()
    rematchees = s.read_people("data/updates/rematchees.json")
    groups = s.read_groups("data/placements/groups.json")

    r = RematchEngine(rematchees, groups)
    r.reassign_mentees()


def main() -> None:
    args = get_args()

    match args.operation:
        case "match":
            initial_match()
        case "rematch":
            rematch()
        case "clean":
            clean()


main()
