from flask import Flask

app = Flask(__name__)

# Define a route with a decorator
@app.route("/")
def index():
    return "<h1>Hello, world</h1>"

# Definte a route with a URL rule (more basic form)
#def index():
#    return "<h1>Hello, world</h1>"
#app.add_url_rule("/", "index", index)

# Adding `path` allows name to contain '/' characters
# which increases the types of XSS you can do
# For example:
# %3Cscript%3Ealert%28%22oops%21%22%29%3B%3C%2Fscript%3E
#@app.route("/user/<path:name>")

# However, because you are still just reflecting the raw user input
# You can also trigger javascript that doesn't require a '/'
# /user/%3Cimg%20src%3Dx%20onerror%3Dalert(1)%3E
@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}</h1>"