import bluerobotics_navigator as navigator
from . import sensors
from . import actuations

class LLCS:
    def __init__(self):
        self.initialize()
        navigator.init()

    def initialize(self):
        actuations.set_pwm_freq_hz(54.28)
        print("LLCS initialized")

    def calibrate(self):
        print("Calibrating...")

    def read_and_print_angles(self):
        sensors.read_and_print_angles()

    def get_pitch(self) -> float:
        return sensors.get_pitch()

    def actuation(self, input, neutranInput, forwardMaxInput, backwardMaxInput):
        actuations.actuation(input, neutranInput, forwardMaxInput, backwardMaxInput)

    def onShutdown(self, neutralInput):
        actuations.actuation(neutralInput, neutralInput, neutralInput, neutralInput)
        navigator.set_pwm_enable(False)
        print("LLCS shutdown")