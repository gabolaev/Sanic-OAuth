"""
    Non-Working Example for Initial Reference
    By: Shawn Niederriter
    GitHub: https://github.com/Sniedes722
    Inspired by Flask-OAuthLib's Google Client Example
"""
from sanic import Sanic
from sanic.response import json
from sanic_session import InMemorySessionInterface
from sanic_envconfig import EnvConfig
from sanic_oauth import OAuthClient

class Config(EnvConfig):
    HOST: str = None
    PORT: int = 4
    DEBUG: bool = True
    WORKERS: int = 1
    GOOGLE_ID: str = None
    GOOGLE_SECRET: str = None
    SECRET_KEY: str = None

app = Sanic()
app.config.from_object(Config)
session_interface = InMemorySessionInterface()
oauth = OAuthClient(app,session_interface)

google = oauth.remote_app(
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

@google.tokengetter
@app.middleware
async def get_google_oauth_token():
    return session.get('google_token')

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
    async def index(request):
        if request['session'].get('google_token'):
            user = google.get('userinfo')
            return json({"data": user.data})
        else:
            return redirect(url_for('login')) ## routing

    @app.route("/login")
    async def login(request):
        return google.authorize(callback=url_for('authorized', _external=True))
    
    
    @app.route("/logout") ## This is probably going to be response middleware
    async def logout(request):
        session.pop('google_token', None) ## Interacts with a dict
        return redirect(url_for('index')) ##url for is routing
    
    @app.route("/login/authorized")
    async def authorized(request):
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    user = google.get('userinfo')
    return json({"data": user.data})
    

    if __name__ == "__main__":
        app.run(host=app.config.HOST, port=app.config.PORT, debug=app.config.DEBUG, workers=app.config.WORKERS)