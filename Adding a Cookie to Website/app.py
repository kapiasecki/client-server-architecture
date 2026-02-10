from flask import Flask, request
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Practicing Cookies!</h1>"

@app.route("/addCookie")
def addCookie():
    response = make_response("<h1>Cookie added!</h1>");
    # add code to add cookie here
    response.set_cookie("myFirstCookie", "Hello World - my first cookie!")
    return response

@app.route("/displayCookieValue")
def displayCookieValue():
    cookieValue = None
    try:
        # Get the cookie value using the correct method
        cookieValue = request.cookies.get('myFirstCookie')

        if cookieValue:
            return "<h1>Cookie value: " + cookieValue + "</h1>"
        #else:
            #return "<h1>Cookie not found!</h1>"
    except:
        return "<h1>Cookie not found!</h1>"
    

@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res

app.run(host='0.0.0.0', port=88)

