import RPi.GPIO as gpio

from models import Config

config = Config()


def setup():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)


def teardown():
    gpio.cleanup()
