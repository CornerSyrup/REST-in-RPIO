import atexit
import utils

utils.setup()
atexit.register(utils.teardown)
