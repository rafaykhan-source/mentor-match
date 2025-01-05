"""The noxfile for the application serves to standardize project tooling."""

import nox


@nox.session
def tests(session):
    session.install(".[test]")
    session.run("pytest")
