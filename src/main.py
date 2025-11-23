from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
import starlette.status as status

from .api import conversations, messages, webhooks

app = FastAPI()
app.include_router(conversations.router)
app.include_router(webhooks.router)
app.include_router(messages.router)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)



