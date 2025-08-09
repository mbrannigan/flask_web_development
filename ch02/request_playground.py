from flask import Flask
from flask import request

# current_app is the details about the application
# request contains the details from the web request
# g is a scratch area for the single request (it's reset each request)
# session is a scratch area that persists between requests for a single user

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    data = request.environ
    return f'<p>Your browser is: {user_agent} {data}</p>'
