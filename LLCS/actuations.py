import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel

if __name__ == "__main__":
    print("This script is not meant to be run directly")

def actuation(input, neutranInput, forwardMaxInput, backwardMaxInput):
    # navigator.set_pwm_freq_hz(1000)
    navigator.set_pwm_channel_value(PwmChannel.Ch1, input)
    if input > neutranInput:
        navigator.set_neopixel([[0, int((input - neutranInput) / (forwardMaxInput - neutranInput) * 128), 0]])
    elif input == neutranInput:
        navigator.set_neopixel([[0, 0, 0]])
    else:
        navigator.set_neopixel([[int((neutranInput - input) / (neutranInput - backwardMaxInput) * 128), 0, 0]])
    navigator.set_pwm_enable(True)

def set_pwm_freq_hz(freq):
    print("Set PWM Frea Hz to 1000")
    navigator.set_pwm_freq_hz(freq)