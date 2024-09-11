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
    pid_controller = HLCS.pid.PIDController()

    llcs.calibrate()
    pwm_value_neutral = 365
    pwm_value_max_forward_clockwise = 437
    pwm_value_max_backword_anticlockwise = 237
    pwm_value = pwm_value_neutral
    pwm_step = 20
    pwm_toggle = True

    for i in range(45):

        pid_output = pid_controller.update(hlcs.target, llcs.get_pitch(), time.time())
        print(f"PID output: {pid_output}")
        pwm_value = int(pwm_value_neutral + pid_output)

        llcs.read_and_print_angles()
        llcs.actuation(pwm_value, pwm_value_neutral, pwm_value_max_forward_clockwise, pwm_value_max_backword_anticlockwise)
        #if (pwm_value + pwm_step >= pwm_value_max_forward_clockwise):
        #    pwm_toggle = False
        #elif (pwm_value - pwm_step <= pwm_value_max_backword_anticlockwise):
        #    pwm_toggle = True
        #if pwm_toggle:
        #    pwm_value += pwm_step
        #else:
        #    pwm_value -= pwm_step
        time.sleep(0.2)

    llcs.onShutdown(pwm_value_neutral)


if __name__ == "__main__":
    main()
