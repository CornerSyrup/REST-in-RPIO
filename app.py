import time

import dht11
import flask
import RPi.GPIO as gpio

import utils

app = flask.Flask(__name__)


@app.route("/")
def index():
    return open("static/index.html", "r").read()


@app.route("/on/<string:device>")
def turn_on(device: str):
    gpio.output(utils.DEV[device], gpio.HIGH)
    return str(gpio.input(utils.DEV[device]))


@app.route("/off/<string:device>")
def turn_off(device: str):
    gpio.output(utils.DEV[device], gpio.LOW)
    return str(gpio.input(utils.DEV[device]))


@app.route("/weather/<string:reading>")
def weather_reading(reading: str):
    reader = dht11.DHT11(utils.SENSOR["weather"])
    result = reader.read()
    time_st = time.time()
    while (not result.is_valid()) and time_st - time.time() < 1:
        result = reader.read()

    return str(result.humidity if (reading == "humid") else result.temperature)


if __name__ == "__main__":
    import __init__

    app.run()
