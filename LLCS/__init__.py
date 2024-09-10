import bluerobotics_navigator as navigator
from . import sensors

class LLCS:
    def __init__(self):
        self.initialize()
        navigator.init()

    def initialize(self):
        print("LLCS initialized")

    def calibrate(self):
        print("Calibrating...")

    def read_and_print_angles(self):
        sensors.read_and_print_angles()