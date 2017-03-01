from sanic import Sanic
from sanic.response import json,html
from airbnb import Api

app = Sanic()

html_body = """<!DOCTYPE html>
<html>
<body>
<h1>Airbnb Login</h1>
<form action="/profile" method="HEAD">
  First name:<br>
  <input type="text" name="user" value="">
  <br>
  Last name:<br>
  <input type="password" name="pass" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 


</body>
</html>"""

@app.route("/",methods=['GET'])
async def index(request):
    return html(html_body)


@app.route("/profile",methods=['GET','POST'])
async def profile(request):
    info = dict(request.args)
    #user = str(info['user']).replace("['","").replace("']","")
    #password = str(info['pass']).replace("['","").replace("']","")
    #bnb = Api(user,password)
    #profile = bnb.get_profile()
    return json(info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)