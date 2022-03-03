import atexit
import config

config.setup()
atexit.register(config.teardown)
