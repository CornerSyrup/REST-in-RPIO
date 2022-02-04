import time

import dht11
import flask
import RPi.GPIO as gpio

import config

app = flask.Flask(__name__)


@app.route("/")
def index():
    return open("static/index.html", "r").read()


@app.route("/on/<string:device>")
def turn_on(device: str):
    pin = next(x.pin for x in config.devices if x.name == device and x.mode)
    gpio.output(pin, gpio.HIGH)
    return str(gpio.input(pin))


@app.route("/off/<string:device>")
def turn_off(device: str):
    pin = next(x.pin for x in config.devices if x.name == device and x.mode)
    gpio.output(pin, gpio.LOW)
    return str(gpio.input(pin))


@app.route("/weather/<string:reading>")
def weather_reading(reading: str):
    dev = next(x for x in config.devices if x.name == "weather")
    reader = dht11.DHT11(dev.pin)
    result = reader.read()
    time_st = time.time()
    while (not result.is_valid()) and time.time() - time_st < 2.5:
        result = reader.read()

    return str(result.humidity if (reading == "humid") else result.temperature)


if __name__ == "__main__":
    import __init__

    app.run()
