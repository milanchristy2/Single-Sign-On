from httpcore import request

from database import Session
from models import User
from fastapi import APIRouter,Request
from oauth import oauth

router=APIRouter()

db=Session()

@router.get("/")
def home():
    return "Hello"

@router.get("/login")
async def login(request:Request):
    redirect_uri="http://localhost:8000/auth"
    # print("REDIRECT URI:", redirect_uri)
    return await oauth.github.authorize_redirect(request,redirect_uri=redirect_uri)

@router.get("/auth",name="auth")
async def auth(request:Request):
    token=await oauth.github.authorize_access_token(request)
    resp=await oauth.github.get("user",token=token)
    profile=resp.json()
    github_id=profile.get("id")
    username=profile.get("login")
    user=db.query(User).filter(User.github_id==github_id).first()

    if not user:
        user=User(
            github_id=github_id,
            name=username
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()

    return {
        "github_id": user.github_id,
        "username":user.name
    }

