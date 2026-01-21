from fastapi import FastAPI
from router.routes import router
from starlette.middleware.sessions import SessionMiddleware
import os
import uvicorn

app=FastAPI()

app.add_middleware(SessionMiddleware,secret_key=os.getenv("SECRET_KEY"))

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


