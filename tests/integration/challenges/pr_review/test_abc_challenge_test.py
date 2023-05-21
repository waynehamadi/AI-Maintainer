from types import SimpleNamespace
import pytest

from tests.integration.challenges.pr_review.base import run_tests

PR_LINK = "https://github.com/merwanehamadi/Auto-GPT/pull/141"
PARAMETERS = SimpleNamespace(
    source_branch_name="abc-challenge-test",
    source_repo_user="merwanehamadi",

    # PR information
    title="abc-challenge-test",
    body="abc-challenge-test",

    # PR success criteria
    approved=False,
    contains={"tests/integration/challenges/pr_review/props/bad_abc.py": ["implement"]},
)
# @pytest.skip("skip")
def test_abc_challenge_test(

) -> None:
    run_tests(PARAMETERS)
