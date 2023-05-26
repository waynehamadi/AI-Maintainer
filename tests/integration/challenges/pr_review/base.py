import os
from datetime import datetime
from reviewer import review_pr, load_envs
from github import Github

from collections import defaultdict
PR_TARGET_BRANCH = "hackathon-pr-target"
PR_TARGET_REPO_USER = "merwanehamadi"
REPO_NAME = "Auto-GPT"
PR_TARGET_REPO = f"{PR_TARGET_REPO_USER}/{REPO_NAME}"
GITHUB_CREATOR_TOKEN = os.environ.get("GITHUB_CREATOR_TOKEN")
GITHUB_REVIEWER_TOKEN = os.environ.get("GITHUB_REVIEWER_TOKEN")
from collections import defaultdict
from datetime import datetime

def create_pr(
        source_branch_name,
        source_repo_user,
        title,
        body
    ):
    # First create a Github instance with your token:

    g = Github(GITHUB_CREATOR_TOKEN)

    # Then get your repository:
    repo = g.get_user(source_repo_user).get_repo(REPO_NAME)

    # Get the branch you want to copy

    base_branch = repo.get_branch(source_branch_name)

    # Create the name for the new branch
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_branch_name = f"{source_branch_name}-{timestamp}"

    # Create the new branch
    repo.create_git_ref(ref=f"refs/heads/{new_branch_name}", sha=base_branch.commit.sha)
    title = f"{os.environ.get('TEAM_MEMBER_NAME')} {title}"
    # Create a new pull request
    pr = repo.create_pull(
        title=title,
        body=body,
        head=new_branch_name,
        base=PR_TARGET_BRANCH,
    )

    return pr.number


def check_pr(pr_number, parameters):
    # First create a Github instance with your token:
    g = Github(GITHUB_CREATOR_TOKEN)

    # Get the repository
    repo = g.get_user(PR_TARGET_REPO_USER).get_repo(REPO_NAME)

    # Get the pull request
    pr = repo.get_pull(pr_number)

    # Count approvals
    approvals = 0

    # Get reviews for the pull request
    for review in pr.get_reviews():
        # Check if the review is an approval
        if review.state == "APPROVED":
            approvals += 1

    # Get file comments
    check_last_review(parameters, pr, pr_number, PR_TARGET_REPO)

    print(
        f"The PR number {pr_number} in the repository {PR_TARGET_REPO} has {approvals} approvals."
    )
    if hasattr(parameters, "approved"):
        if parameters.approved:
            assert approvals > 0
        else:
            assert approvals == 0

    return True  # All conditions were satisfied

def check_last_review(parameters, pr, pr_number, PR_TARGET_REPO):
    reviews = pr.get_reviews().get_page(0)

    # if there's no review, return
    if not reviews:
        assert False, "No review found for this PR."

    # Get the last review
    last_review = reviews[-1]
    review_time = last_review.submitted_at

    # get current time
    now = datetime.utcnow()

    # Check if it was submitted within last 10 seconds
    assert (now - review_time).total_seconds() <= 10, \
        f"The latest review on PR number {pr_number} in the repository {PR_TARGET_REPO} was not submitted within the last 10 seconds."

    # Check if all required comments are present in the last review
    required_comments = parameters.review_contains
    for required_comment in required_comments:
        assert required_comment in last_review.body, \
            f"Missing required comment '{required_comment}' in the last review of PR number {pr_number} in the repository {PR_TARGET_REPO}."



def run_tests(parameters):
    load_envs()
    pr_number = create_pr(
        parameters.source_branch_name,
        parameters.source_repo_user,
        parameters.title,
        parameters.body,
    )

    api_url = 'https://api.github.com/repos/merwanehamadi/Auto-GPT/pulls/' + str(pr_number)
    'https://github.com/octocat/Hello-World/pull/1347.diff'
    diff_url = "https://github.com/merwanehamadi/Auto-GPT/pull/"
    diff_url += str(pr_number) + ".diff"
    review_pr(api_url, diff_url, parameters.title, parameters.body)
    # call_api(pr_number)

    check_pr(pr_number, parameters)
