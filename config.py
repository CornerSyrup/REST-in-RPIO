import RPi.GPIO as gpio

from models import Device

devices = [
    Device("living", 17),
    Device("kitchen", 27),
    Device("tv", 22),
    Device("weather", 18, False),
]


def setup():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    for dev in devices:
        gpio.setup(dev.pin, gpio.OUT if dev.mode else gpio.IN)


def teardown():
    gpio.cleanup()
