from flask import Flask

app = Flask(__name__)


@app.roue('/')
def index():
    return "Hello User, Welcome to Flask Tutorial"


app.run(debug=True)
