import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel

if __name__ == "__main__":
    print("This script is not meant to be run directly")

def actuation(input, neutranInput, forwardMaxInput, backwardMaxInput):
    # navigator.set_pwm_freq_hz(1000)
    navigator.set_pwm_channel_value(PwmChannel.Ch1, input)
    if input > neutranInput:
        navigator.set_neopixel([[int((input - neutranInput) / (forwardMaxInput - neutranInput)), 0, 0]])
    elif input == neutranInput:
        navigator.set_neopixel([[0, 0, 0]])
    else:
        print(f"input: {input}, neutranInput: {neutranInput}, forwardMaxInput: {forwardMaxInput}, backwardMaxInput: {backwardMaxInput}")
        navigator.set_neopixel([[0, int((input - backwardMaxInput) / (neutranInput - backwardMaxInput)), 0]])
    navigator.set_pwm_enable(True)

def set_pwm_freq_hz(freq):
    print("Set PWM Frea Hz to 1000")
    navigator.set_pwm_freq_hz(freq)