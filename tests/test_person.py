from mentor_match.models import Person


def test_person_equality(john):
    assert john == Person(
        "John",
        "Doe",
        "jd@email.com",
        ["3:00-4:00pm M", "3:00-4:00pm T"],
    )
    assert john == Person(
        "John",
        "D",
        "jd@email.com",
        ["3:00-4:00pm M", "3:00-4:00pm T"],
    )
