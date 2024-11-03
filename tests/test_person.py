from mentor_match.models import Person


def test_person_equality() -> None:
    a = Person("John", "Doe", "jd@email.com", ["3:00-4:00pm M", "3:00-4:00pm T"])
    assert a == Person(
        "John",
        "Doe",
        "jd@email.com",
        ["3:00-4:00pm M", "3:00-4:00pm T"],
    )
