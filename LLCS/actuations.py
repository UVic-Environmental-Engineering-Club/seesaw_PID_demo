import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel

def __init__():
    print("Set PWM Frea Hz to 1000")
    navigator.set_pwm_freq_hz(1000)

def actuation(input):
    # navigator.set_pwm_freq_hz(1000)
    navigator.set_pwm_channel_value(PwmChannel.Ch1, input)
    navigator.set_neopixel([[int((2000 - input) / 1600) * 255, 0, 0]])
    navigator.set_pwm_enable(True)