from flask import Flask  # imported Flask class from flask module

app = Flask(__name__)  # app is an instance


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/about")
def about():
    me = {
        "first_name": "DeVonte",
        "last_name": "Gray",
        "age": 30,
        "home": "Georgia",
        "hobby": "Video Games, Experiments"
    }
    return me
