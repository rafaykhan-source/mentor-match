from mentor_match.models import Group


def test_group(john):
    g = Group(john, john.availability[1])
    assert g == Group(john, john.availability[1])
    assert Group(john, john.availability[0]) != Group(john, john.availability[1])
    assert g.meeting_time in g.mentor.availability
