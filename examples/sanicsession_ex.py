from sanic import Sanic
from sanic.response import text
from sanic_session import InMemorySessionInterface


app = Sanic()
session_interface = InMemorySessionInterface()

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
    # interact with the session like a normal dict
    if not request['session'].get('foo'):
        request['session']['foo'] = 0

    request['session']['foo'] += 1

    return text(request['session']['foo'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)