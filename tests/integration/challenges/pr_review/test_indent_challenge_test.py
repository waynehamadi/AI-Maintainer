from types import SimpleNamespace
import pytest

from tests.integration.challenges.pr_review.base import run_tests

PR_LINK = "https://github.com/merwanehamadi/Auto-GPT/pull/133"
PARAMETERS = SimpleNamespace(
    source_branch_name="indent-challenge-test",
    source_repo_user="merwanehamadi",

    # PR information
    title="indent-challenge-test",
    body="indent-challenge-test",

    # PR success criteria
    review_contains=[],
    # contains={"bad_variable_name.py": ["variable"]},
)


def test_indent_challenge_test(

) -> None:
    run_tests(PARAMETERS)
