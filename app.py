import flask

from devices import devices
from models import JsonEncoder

app = flask.Flask(__name__)
app.json_encoder = JsonEncoder
app.register_blueprint(devices, url_prefix="/devices")


@app.route("/")
def index():
    return open("static/index.html", "r").read()


if __name__ == "__main__":
    import __init__

    app.run()
