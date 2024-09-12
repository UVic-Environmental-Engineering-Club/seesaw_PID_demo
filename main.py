
import HLCS
import LLCS
import sys
import time
import math
import threading

running = True

hlcs = HLCS.HLCS()
llcs = LLCS.LLCS()
pid_controller = HLCS.pid.PIDController()

def input_listener():
    global running

    # while running:
    user_input = input()
    running = False
    # if user_input.lower() == 'q':
    #     pass


def control_loop():
    global hlcs
    global llcs
    global running
    global pid_controller

    while running:
        pid_output = pid_controller.update(hlcs.target, llcs.get_pitch(), time.time())
        print(f"PID output: {pid_output}")

        llcs.read_and_print_angles()
        llcs.update(pid_output)
        time.sleep(0.2)



def main():
    global hlcs
    global llcs
    global pid_controller

    pid_kp = float(input("Enter the value of Kp: "))
    pid_ki = float(input("Enter the value of Ki: "))
    pid_kd = float(input("Enter the value of Kd: "))
    pid_controller = HLCS.pid.PIDController(kp = pid_kp, ki = pid_ki, kd = pid_kd, integral_limit = 1, output_limit = 1)

    llcs.calibrate()

    input_thread = threading.Thread(target=input_listener)
    control_loop_thread = threading.Thread(target=control_loop)
    input_thread.start()
    control_loop_thread.start()

    input_thread.join()
    control_loop_thread.join()

    llcs.onShutdown()


if __name__ == "__main__":
    main()
