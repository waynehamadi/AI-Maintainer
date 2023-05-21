from types import SimpleNamespace
import pytest

from tests.integration.challenges.pr_review.base import run_tests

PARAMETERS = SimpleNamespace(
    source_branch_name="unused-variable",
    source_repo_user="merwanehamadi",

    # PR information
    title="unused-variable",
    body="unused-variable",

    # PR success criteria
    approved=False,
    # contains={"bad_variable_name.py": ["variable"]},
)


def test_unused_variable(

) -> None:
    run_tests(PARAMETERS)
