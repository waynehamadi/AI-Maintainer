from types import SimpleNamespace

from tests.integration.challenges.pr_review.base import run_tests

# PR_LINK = "https://github.com/merwanehamadi/Auto-GPT/pull/116"
PARAMETERS = SimpleNamespace(
    source_branch_name="useless-comment",
    source_repo_user="merwanehamadi",
    # pr_link=PR_LINK,

    # PR information
    title="Useless comment",
    body="Useless comment",

    # PR success criteria
    pr_number=116,
    review_contains=["comment"]
)


def test_basic_pr_review() -> None:
    run_tests(PARAMETERS)
