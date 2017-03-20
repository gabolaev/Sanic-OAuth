"""
    Non-Working Example for Initial Reference
    By: Shawn Niederriter
    GitHub: https://github.com/Sniedes722
    
    Environs:
    HOST = "0.0.0.0"
    PORT = 8080
    DEBUG = false
    WORKERS = 4
    CLIENT_ID = 
    CLIENT_SECRET = 
"""
from sanic import Sanic
from sanic.response import json
from sanic_session import InMemorySessionInterface
from sanic_envconfig import EnvConfig
from sanic_oauth import OAuthSession

class Config(EnvConfig):
    HOST: str = None
    PORT: int = 4
    DEBUG: bool = True
    WORKERS: int = 1
    CLIENT_ID: str = None
    CLIENT_SECRET: str = None
    SECRET_KEY: str = None

app = Sanic()
app.config.from_object(Config)
session_interface = InMemorySessionInterface()
oauth = OAuthSession(app,session_interface)

google = oauth.provider(
    'google',
    consumer_key=app.config.GOOGLE_ID,
    consumer_secret=app.config.GOOGLE_SECRET,
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

app = Sanic()
session_interface = InMemorySessionInterface()
oauth_interface = OAuthSession(app,'a91k2n3j',session_interface)

@app.middleware('request')
    async def add_session_to_request(request):
        # before each request initialize a session
        # using the client's request
        await session_interface.open(request)


@app.middleware('response')
async def save_session(request, response):
    # after each request save the session,
    # pass the response to set client cookies
    await session_interface.save(request, response)

@app.route("/")
async def test(request):
    if request.headers['X-OAuth-token'] == oauth_interface.client_key:
        return json({"client_key": oauth_interface.client_key})
    else:
        return json({"404 Error":"Not Authorized"})

if __name__ == "__main__":
