# Sanic-OAuth 0.0.5

### Overview
Still in development, WORKING BUILD in package installer by 0.1.0

### OAuth Middleware Extension for Sanic
- Inspired by flask-oauthlib, relies heavily on oauthlib
- OAuthClient for remote apps with OAuth2 (OAuth 1.0,1.1 by 0.2.0)
- OAuthProvider for creating your own OAuth2 token providers (See example)
- Built-in support for Sanic Sessions


### Provider Example w/ Sanic Sessions
```
from sanic import Sanic
from sanic.response import json
from sanic_oauth import OAuthProvider


app = Sanic()
session_interface = InMemorySessionInterface()
token_interface = OAuthProvider(app,session_interface,client_key='GOTTA',client_secret='GO',secret_key='FAST')

@app.middleware('request')
async add_token_to_request(request):
    return token_interface.open(request)


@app.middleware('response')
async save_token_to_session(request,response):
    return token_interface.save(request, response)

@app.route("/")
async def index(request):
    if not request['session'].get('token'):
            request['session']['token'] = token_interface.generate(request,auth_type='2')
        return json({"token": request['session']['token'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

### TODO
- Add to Package Installer
- OAuth1 Support
- Build your own token provider
- Examples for authenticating with Airbnb, Facebook, Google, & Twitter
- Support for Redis


