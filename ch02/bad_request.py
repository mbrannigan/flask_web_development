from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Bad request</p>", 400, {'foo': 'bar'}