from time import time

import RPi.GPIO as gpio
from flask import Blueprint, request

from config import config

pins = Blueprint(__name__, __name__)


@pins.route("/<int:pin>", methods=["POST"])
def switch_state(pin: int):
    req = request.json
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, gpio.HIGH if req["state"] else gpio.LOW)
    return {"state": gpio.input(pin)}


@pins.route("/dev/<string:dev>", methods=["PUT"])
def switch_device_state(dev: str):
    pin = next(x.pin for x in config.devices if x.name == dev and x.mode)
    return switch_state(pin)
