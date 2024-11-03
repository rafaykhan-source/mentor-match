# Mentor Match

An algorithm to form mentorship groups between student mentees and mentors.

## Algorithmic Overview
Provided the availability of mentees and mentors, fix a time for a mentor to have a mentorship group based on their availability (phase one), and assign mentees to that mentorship group if it is also in their availability. We let availability denote a collection of one hour timeslots on a specific day.

## Abstract Datatypes
- Person
- Group

## Development Setup
The project uses `ruff`, `mypy`, and `pre-commit` for linting, formatting, type-checking, and code consistency checks. You can install all of these tools using `uv tool install` and run them on the project where the respective tool configurations are stored in the `pyproject.toml`.

Setup the virtual environment:
```
uv venv
```

Setup testing:
```
uv pip install -e .[test]
```

Setup pre-commit:
```
pre-commit autoupdate
pre-commit install
pre-commit run -a
```

## Program Usage
```
uv run src/mentor_match
```