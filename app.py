from fastapi import FastAPI, APIRouter, HTTPException, Request, Response
from reviewer import review_pr

router = APIRouter()

@router.post("/github_webhooks")
async def handle_github_webhooks(request: Request, response: Response):
    print("Received a github webhook")
    body = await request.json()
    print(body)
    action = body.get("action", None)
    # number = body.get("number", None)
    pull_request = body.get("pull_request", {})
    if action == "opened":
        html_url = pull_request.get("html_url", None)
        if html_url is None:
            return {}
        try:
            review_pr(html_url)
        except Exception as e:
            print(e)
    return {}
        
        

app = FastAPI()
app.include_router(router, prefix="/api/v1")