import RPi.GPIO as gpio

DEV = {"living": 17, "kitchen": 27, "tv": 22}


def setup():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    for id in DEV:
        gpio.setup(DEV[id], gpio.OUT)


def teardown():
    gpio.cleanup()
