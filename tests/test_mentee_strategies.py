from mentor_match.mentee_strategies import RandomGroupStrategy, SmallestGroupStrategy


def test_mentee_time_assignments_not_empty_random_smallest(random_times) -> None:
    groups, mentees = random_times

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        assert g.meeting_time != ""


def test_mentee_time_assignments_from_availability_random_smallest(
    random_times,
) -> None:
    groups, mentees = random_times

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        for m in g.mentees:
            assert g.meeting_time in m.availability


def test_mentee_time_assignments_not_empty_random_random(random_times) -> None:
    groups, mentees = random_times

    r = RandomGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        assert g.meeting_time != ""


def test_mentee_time_assignments_from_availability_random_random(random_times) -> None:
    groups, mentees = random_times

    r = RandomGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        for m in g.mentees:
            assert g.meeting_time in m.availability


def test_mentee_time_assignments_not_empty_frequency(frequency_times) -> None:
    groups, mentees = frequency_times

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        assert g.meeting_time != ""


def test_mentee_time_assignments_from_availability_frequency(frequency_times) -> None:
    groups, mentees = frequency_times

    r = SmallestGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        for m in g.mentees:
            assert g.meeting_time in m.availability


def test_mentee_time_assignments_not_empty_frequency_random(frequency_times) -> None:
    groups, mentees = frequency_times

    r = RandomGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        assert g.meeting_time != ""


def test_mentee_time_assignments_from_availability_frequency_random(
    frequency_times,
) -> None:
    groups, mentees = frequency_times

    r = RandomGroupStrategy(groups, mentees)
    r.assign_mentees()

    for g in groups:
        for m in g.mentees:
            assert g.meeting_time in m.availability
