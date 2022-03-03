import flask

from devices import devices
from models import JsonEncoder
from pins import pins
from settings import settings

app = flask.Flask(__name__)
app.json_encoder = JsonEncoder
app.register_blueprint(devices, url_prefix="/devices")
app.register_blueprint(settings, url_prefix="/settings")
app.register_blueprint(pins, url_prefix="/pins")


@app.route("/", defaults={"path": None})
@app.route("/<path:path>")
def index(path: str):
    return open("static/index.html", "r").read()


if __name__ == "__main__":
    import __init__

    app.run()
