from time import time

import RPi.GPIO as gpio
from dht11 import DHT11
from flask import Blueprint, request

from config import config

devices = Blueprint(__name__, __name__)


@devices.route("/", methods=["GET"])
def get_devices():
    return {"devices": config.devices}


@devices.route("/", methods=["POST"])
def add_devices():
    req = request.json
    config.new_dev(req["name"], req["pin"])
    return {}


@devices.route("/weather/<string:reading>")
def weather_reading(reading: str):
    dev = next(x for x in config.devices if x.name == "weather")
    reader = DHT11(dev.pin)
    result = reader.read()
    time_st = time()
    while (not result.is_valid()) and time() - time_st < 2.5:
        result = reader.read()

    return str(result.humidity if (reading == "humid") else result.temperature)


@devices.route("/<string:dev>", methods=["PUT"])
def switch_device_state(dev: str):
    req = request.json
    pin = next(x.pin for x in config.devices if x.name == dev and x.mode)
    gpio.output(pin, gpio.HIGH if req["state"] else gpio.LOW)
    return {"state": gpio.input(pin)}
