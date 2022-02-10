import RPi.GPIO as gpio

from models import Config

config = Config()


def setup():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    for dev in config.devices:
        gpio.setup(dev.pin, gpio.OUT if dev.mode else gpio.IN)


def teardown():
    gpio.cleanup()
