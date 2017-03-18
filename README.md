# Sanic-OAuth
OAuth Interface for Sanic
- Inspired by flask-oauthlib, relies heavily on oauthlib
- OAuthClient for remote apps with OAuth1 & 2
- OAuthSessions for Sanic Sessions
- Built-in helper functions for authenticating with Airbnb, Facebook, Google, & Twitter
- Provides support for building your own providers with OAuth 1 & 2

### Overview
Sanic-OAuth 0.4.0
Still in development, working build in package installer by 0.1.0

### Sessions Example
```
from sanic import Sanic
from sanic.response import json
from sanic_oauth import OAuthSession


app = Sanic()
oauth_interface = OAuthSession(app,'a91k2n3j',session_interface='inmem')

@app.route("/")
async def test(request):
    if request.headers['X-OAuth-token'] == oauth_interface.client_key:
        return json({"client_key": oauth_interface.client_key})
    else:
        return json({"404 Error":"Not Authorized"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

### TODO
- Add to Package Installer
- OAuth1 Support
- OAuth2 Support


