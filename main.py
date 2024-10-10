
import sys
import time
import math

import bluerobotics_navigator as navigator

import LLCS



int_pitch = 0.0
int_roll = 0.0
int_yaw = 0.0
pitch_vel = 0.0
roll_vel = 0.0
yaw_vel = 0.0
prev_time = 0.0


def testing_loop():
    global int_pitch
    global int_roll
    global int_yaw
    global pitch_vel
    global roll_vel
    global yaw_vel
    global prev_time

    next_time = time.time_ns()
    time_delta = (next_time - prev_time) / 1_000_000_000

    (pitch, roll, yaw) = LLCS.sensors.get_pitch_roll_yaw()
    ang_acc = navigator.read_gyro()
    pitch_vel += ang_acc.y * time_delta
    roll_vel += ang_acc.x * time_delta
    yaw_vel += -ang_acc.z * time_delta
    int_pitch += pitch_vel * time_delta
    int_roll += roll_vel * time_delta
    int_yaw += yaw_vel * time_delta

    pitch_error = pitch - int_pitch
    roll_error = roll - int_roll
    yaw_error = yaw - yaw_error

    prev_time = next_time

    
    print(f"Delta: {time_delta:10.7f}, Error: ({pitch_error:10.5f}, {roll_error:10.5f}), Integrated: ({int_pitch:10.5f}, {int_roll:10.5f}), Actual: ({pitch:10.5f}, {roll:10.5f})")




def main():
    global int_pitch
    global int_roll
    global int_yaw
    global prev_time

    navigator.init()

    (int_pitch, int_roll, int_yaw) = LLCS.sensors.get_pitch_roll_yaw()
    
    prev_time = time.time_ns()


    try:
        while True:
            testing_loop()
    finally:
        print("Done")



if __name__ == "__main__":
    main()
