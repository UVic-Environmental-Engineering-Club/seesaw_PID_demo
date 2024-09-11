import bluerobotics_navigator as navigator
from . import sensors
from . import actuators
import HLCS

class LLCS:
    def __init__(self):
        self.initialize()
        navigator.init()

    def initialize(self):
        self.motor = actuators.Motor()
        self.motor.start_up()
        print("LLCS initialized")

    def calibrate(self):
        print("Calibrating...")

    def read_and_print_angles(self):
        sensors.read_and_print_angles()

    def get_pitch(self) -> float:
        return sensors.get_pitch()

    def actuation(self, input):
        self.motor.actuation(HLCS.pid.clamp(input, -1, 1))

    def onShutdown(self):
        self.motor.shut_down()
        print("LLCS shutdown")