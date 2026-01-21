from fastapi_sso.sso.github import GithubSSO
from fastapi import APIRouter,HTTPException,Depends,Request
from db.models import TestUser
from db.database import Session,get_db
import os


github_sso=GithubSSO(
    os.getenv("github_client_id"),
    os.getenv("github_client_secret"),
    os.getenv("github_redirect_uri")
)

router=APIRouter(prefix="/v1/github")

@router.get("/")

def index():
    return {"message":"hello welcome"}

@router.get("/login")
async def login():
    async with github_sso:
        return await github_sso.get_login_redirect()

@router.get("/callback")
async def callback(request:Request,db:Session=Depends(get_db)):
    try:
        async with github_sso:
            guser=await github_sso.verify_and_process(request)
            # token_data=await github_sso.get_token(request)
            # access_token=token_data("access_token")
            if not guser:
                raise HTTPException(status_code=401,detail="github auth not found")

            user=(
                db.query(TestUser).filter(TestUser.id==guser.id).first()
            )
            if not user:
                user=TestUser(
                    github_id=guser.id,
                    name=guser.display_name,
                    # access_token=guser.access_token
                )
            db.add(user)
            db.commit()
            db.refresh(user)

    except Exception as ex:
        raise HTTPException(status_code=400,detail=str(ex))

    return {
        "id":user.id,
        "github_id":user.github_id,
        "username":user.name,
        "access_token":user.access_token,
    }
