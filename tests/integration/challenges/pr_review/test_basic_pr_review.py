from types import SimpleNamespace

import pytest

# 
from tests.integration.challenges.pr_review.base import run_tests

PR_LINK = "https://github.com/merwanehamadi/Auto-GPT/pull/116"
PARAMETERS = SimpleNamespace(
    source_branch_name="useless-comment",
    source_repo_user="merwanehamadi",

    # PR information
    title="Useless comment",
    body="Useless comment",

    # PR success criteria
    approved=False,
)

def test_basic_pr_review() -> None:
    run_tests(PARAMETERS)
