# Sanic-OAuth
OAuth Interface for Sanic

### Overview

### Example
```
from sanic import Sanic
from sanic.response import json
from sanic_oauth import OAuthInterface


app = Sanic()
oauth_interface = OAuthInterface(app,'a91k2n3j',session_interface='inmem')

@app.route("/")
async def test(request):
    if request.headers['OAuth-token'] == oauth_interface.client_key:
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


