from fastapi_sso.sso.github import GithubSSO
from fastapi import APIRouter,HTTPException,Depends,Request,Response
from fastapi.responses import  JSONResponse
from oauthlib.common import extract_params
from starlette.responses import RedirectResponse

from db.models import TestUser
from db.database import Session,get_db
from sqlalchemy.orm import Session
import os


github_sso=GithubSSO(
    client_id=os.getenv("github_client_id"),
    client_secret=os.getenv("github_client_secret"),
    redirect_uri=os.getenv("github_redirect_uri")
)

router=APIRouter(prefix="/v1/github")

@router.get("/")
def index():
    return {"message":"hello welcome"}

@router.get("/login")
async def login(force_login:bool=False):
    # if force_login:
    #     client_id=os.getenv("github_client_id")
    #     # client_secret=os.getenv("github_client_secret")
    #     redirect_uri=os.getenv("github_redirect_uri")
    #     state="random state"
    #     login_url=(
    #         f"https://github.com/login/oauth/authorize"
    #         f"?client_id={client_id}"
    #         f"&redirect_uri={redirect_uri}"
    #         f"&state={state}"
    #         f"&prompt=login"
    #     )
    #     return RedirectResponse(login_url)
    async with github_sso:
        return await github_sso.get_login_redirect()

@router.get("/callback")
async def callback(request:Request,db:Session=Depends(get_db)):
    try:
            guser=await github_sso.verify_and_process(request)
            # token_data=await github_sso.get_token(request)
            # access_token=token_data("access_token")
            if not guser:
                raise HTTPException(status_code=401,detail="github auth not found")

            user=(
                db.query(TestUser).filter(TestUser.github_id==guser.id).first()
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

    response=JSONResponse({
        "id":user.id,
        "github_id":user.github_id,
        "username":user.name,
    })
    response.set_cookie("github_id",str(user.github_id))
    response.set_cookie("username",user.name)
    return response
# @router.get("/logout")
@router.post("/logout")
async def logout(response:Response):
    response.delete_cookie("github_id")
    response.delete_cookie("username")
    return {"message":"logout succcessfully"}
@router.get("/who")
async def whoAmI(request:Request,db:Session=Depends(get_db)):
    github_id=request.cookies.get("github_id")
    if not github_id:
        return {"user":None}
    user=db.query(TestUser).filter(TestUser.github_id==github_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="no user found")
    return {
        "id":user.id,
        "github_id":user.github_id,
        "username":user.name
    }