import RPi.GPIO as gpio

DEV = {"living": 17, "kitchen": 27, "tv": 22}
SENSOR = {"weather": 18}


def setup():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    for id in DEV:
        gpio.setup(DEV[id], gpio.OUT)
    for id in SENSOR:
        gpio.setup(SENSOR[id], gpio.IN)


def teardown():
    gpio.cleanup()
