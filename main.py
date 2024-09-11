import HLCS
import LLCS
import sys
import time
#try:
#    import bluerobotics_navigator as navigator
#except ImportError:
#    raise ImportError("Bluerobotics navigaotor library was not imported\ntry: pip install bluerobotics_navigator")


def main():
    print("Hello World")
    llcs = LLCS.LLCS()
    hlcs = HLCS.HLCS()

    llcs.calibrate()
    pwm_hz = 400
    pwm_toggle = False
    while True:
        llcs.read_and_print_angles()
        llcs.actuation(pwm_hz)
        if (pwm_hz >= 2000):
            pwm_toggle = True
        elif (pwm_hz <= 400):
            pwm_toggle = False
        if pwm_toggle:
            pwm_hz -= 50
        else:
            pwm_hz += 50
        time.sleep(0.5)


if __name__ == "__main__":
    main()
