from flask import Flask  # imported Flask class from flask module

app = Flask(__name__)  # app is an instance


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/about")
def about():
    me = {
        "first_name": "DEVONTE",
        "last_name": "GRAY",
        "age": 30,
        "home": "GEORGIA",
        "hobby": "VIDEO GAMES, Experiments"
    }
    return me
