
#! /bin/python3

import bluerobotics_navigator as brn
import math as np

brn.init()

while True:

    acc = brn.read_accel()
    acc_mag = (acc.x * acc.x + acc.y * acc.y + acc.z * acc.z) ** 0.5
    acc_dir = (acc.x / acc_mag, acc.y / acc_mag, acc.z / acc_mag)
    angle = np.acos(acc_dir[2])

    print(f"Acceleration: ({acc.x:10.5f}, {acc.y:10.5f}, {acc.z:10.5f}), angle: {angle:10.5f}")
