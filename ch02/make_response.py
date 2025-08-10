from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route("/")
def index():
    response = make_response("<p>This is the response</p>")
    response.headers.add("foo", "bar")
    response.status_code = 200
    return response