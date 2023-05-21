from types import SimpleNamespace
import pytest

from tests.integration.challenges.pr_review.base import run_tests

PR_LINK = "https://github.com/merwanehamadi/Auto-GPT/pull/139"
PARAMETERS = SimpleNamespace(
    source_branch_name="exception-challenge-answer",
    source_repo_user="merwanehamadi",

    # PR information
    title="exception-challenge-answer",
    body="exception-challenge-answer",

    # PR success criteria
    approved=False,
    # contains={"bad_variable_name.py": ["variable"]},
)

@pytest.skip("skip")
def test_exception_challenge_answer(

) -> None:
    run_tests(PARAMETERS)
