from fastapi import FastAPI, APIRouter, HTTPException, Request, Response
from reviewer import review_pr

router = APIRouter()

@router.post("/github_webhooks")
async def handle_github_webhooks(request: Request, response: Response):
    print("Received a github webhook")
    try:
        body = await request.json()
    except Exception as e:
        print(e)
        return {}
    print(body)
    pull_request = body.get("pull_request", None)
    if not pull_request:
        return {}
    action = body.get("action", None)
    if action == "opened" or action == "reopened":
        api_url = pull_request.get("url", None)
        diff_url = pull_request.get("diff_url", None)
        title = pull_request.get("title", None)
        description = pull_request.get("body", None)
        owner_username = pull_request.get("user", {}).get("login", None)
        repo_name = pull_request.get("head", {}).get("repo", {}).get("name", None)
        pull_id = pull_request.get("number", None)
        if api_url is None:
            return {}
        msg = review_pr(api_url, diff_url, title, description, owner_username, repo_name, pull_id)
        print(msg)

    return {}
        

app = FastAPI()
app.include_router(router, prefix="/api/v1")