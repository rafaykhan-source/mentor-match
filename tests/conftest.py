import pytest

from mentor_match.models import Person


@pytest.fixture
def john() -> Person:
    return Person("John", "Doe", "jd@email.com", ["3:00-4:00pm M", "3:00-4:00pm T"])


@pytest.fixture
def times() -> list[str]:
    return [
        "5:00-6:00pm Th",
        "3:00-4:00pm Sun",
        "8:00-9:00pm W",
        "6:00-7:00pm Sun",
        "8:00-9:00pm Th",
        "6:00-7:00pm F",
        "4:00-5:00pm Sun",
        "5:00-6:00pm F",
        "7:00-8:00pm Sun",
        "6:00-7:00pm M",
        "7:00-8:00pm Th",
        "7:00-8:00pm T",
        "6:00-7:00pm W",
        "7:00-8:00pm M",
        "8:00-9:00pm T",
        "7:00-8:00pm W",
        "8:00-9:00pm F",
        "5:00-6:00pm T",
        "8:00-9:00pm M",
        "6:00-7:00pm Th",
        "5:00-6:00pm W",
        "5:00-6:00pm M",
        "6:00-7:00pm T",
        "7:00-8:00pm F",
        "8:00-9:00pm Sun",
    ]


@pytest.fixture
def time() -> str:
    return "5:00-6:00pm Th"
