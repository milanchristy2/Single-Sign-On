from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
import os

config = Config(".env")

oauth = OAuth(config)

oauth.register(
    name="github",
    client_id=os.getenv("github_client_id"),
    client_secret=os.getenv("github_client_secret"),
    access_token_url="https://github.com/login/oauth/access_token",
    authorize_url="https://github.com/login/oauth/authorize",
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "read:user"},
)