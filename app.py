from fastapi import FastAPI, APIRouter, HTTPException, Request, Response

router = APIRouter()

@router.post("/github_webhooks")
async def handle_github_webhooks(request: Request, response: Response):
    print("Received a github webhook")
    body = await request.json()
    print(body)
    return {}

app = FastAPI()
app.include_router(router, prefix="/api/v1")