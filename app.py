import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return open("static/index.html", "r").read()


if __name__ == "__main__":
    app.run()
