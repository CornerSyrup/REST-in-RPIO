from flask import Blueprint

from config import config

settings = Blueprint(__name__, __name__)


@settings.route("/save")
def save_setting():
    config.save_config()
    return {}


@settings.route("/reload")
def reload_setting():
    config.load_config()
    return {}
