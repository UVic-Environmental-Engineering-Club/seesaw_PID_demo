import bluerobotics_navigator as navigator
from . import sensors
from . import actuators
import HLCS

class LLCS:
    def __init__(self):

        self.max_motor_input = 0.1
        self.min_motor_input = 0.05
        self.bump_motor_input = 0.1
        self.motor_input_converge_factor = 0.8

        self.current_motor_input = 0
        self.target_motor_input = 0

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

    def actuate(self):

        self.motor.actuate(self.target_motor_input)


    def update(self, input):

        # We need to "bump" the motor to overcome static friction
        #if abs(input) < self.min_motor_input:
        #    if input < 0:
        #        self.target_motor_input = -self.bump_motor_input
        #    else:
        #        self.target_motor_input = self.bump_motor_input

        # self.current_motor_input = HLCS.pid.lerp(self.current_motor_input, self.target_motor_input, self.motor_input_converge_factor)

        self.target_motor_input = HLCS.pid.clamp_mag(input, self.max_motor_input)
        print(f"target motor input: {self.target_motor_input}")

        #if abs(self.target_motor_input) < self.min_motor_input:
        #    self.current_motor_input = 0

        self.actuate()


    def onShutdown(self):
        self.motor.shut_down()
        print("LLCS shutdown")