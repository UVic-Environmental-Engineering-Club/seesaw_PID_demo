import bluerobotics_navigator as navigator
from . import sensors
from . import actuators
import HLCS

class LLCS:
    def __init__(self):

        self.max_motor_input = 0.7

        self.initialize()
        navigator.init()

    def initialize(self):
        self.motor = actuators.Motor()
        self.neo_pixel = actuators.NeoPixel()
        self.motor.start_up()
        print("LLCS initialized")

    def calibrate(self):
        print("Calibrating...")

    def read_and_print_angles(self):
        sensors.read_and_print_angles()

    def get_pitch(self) -> float:
        return sensors.get_pitch()

    def actuation(self, input):

        limited_input = HLCS.pid.clamp_mag(input, self.max_motor_input)

        self.neo_pixel.actuate(limited_input)
        self.motor.actuate(limited_input)

    def onShutdown(self):
        self.motor.shut_down()
        print("LLCS shutdown")