from mentor_match.mentor_strategies import FrequencyTimeStrategy, RandomTimeStrategy


def test_mentor_time_assignments_not_empty_random(prepared_people) -> None:
    mentors, mentees, groups = prepared_people

    r = RandomTimeStrategy(groups, mentees)
    r.set_meeting_times()

    for g in groups:
        assert g.meeting_time != ""


def test_mentor_time_assignments_from_availability_random(prepared_people) -> None:
    mentors, mentees, groups = prepared_people

    r = RandomTimeStrategy(groups, mentees)
    r.set_meeting_times()

    for g in groups:
        assert g.meeting_time in g.mentor.availability


def test_mentor_time_assignments_not_empty_frequency(prepared_people) -> None:
    mentors, mentees, groups = prepared_people

    r = FrequencyTimeStrategy(groups, mentees)
    r.set_meeting_times()

    for g in groups:
        assert g.meeting_time != ""


def test_mentor_time_assignments_from_availability_frequency(prepared_people) -> None:
    mentors, mentees, groups = prepared_people

    r = RandomTimeStrategy(groups, mentees)
    r.set_meeting_times()

    for g in groups:
        assert g.meeting_time in g.mentor.availability
