from mentor_match.models import Person


def test_person_equality(john):
    assert john == Person(
        first_name="John",
        last_name="Doe",
        email="jd@email.com",
        username="jd1334",
        availability=["3:00-4:00pm M", "3:00-4:00pm T"],
    )
    assert john == Person(
        first_name="John",
        last_name="Doe",
        email="jd@email.com",
        username="jd1334",
        availability=["3:00-4:00pm M", "3:00-4:00pm T"],
    )
