import os

import httpx
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
from routes import router

app=FastAPI()

app.add_middleware(SessionMiddleware,secret_key=os.getenv("SESSION_SECRET"))
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)