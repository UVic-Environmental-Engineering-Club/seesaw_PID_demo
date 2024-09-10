
#! /bin/python3

import bluerobotics_navigator as brn
import math as np

brn.init()

while True:

    # Get acceleration from the NFC, note that positive z is down
    acc = brn.read_accel()

    # Normalize the acceleration vector
    acc_mag = (acc.x * acc.x + acc.y * acc.y + acc.z * acc.z) ** 0.5
    acc_dir = (0, 0, 0)
    if (acc_mag > 0.0001):
        acc_dir = (acc.x / acc_mag, acc.y / acc_mag, acc.z / acc_mag)

    

    # Use the dot product angle formula to get the angle (in radians) of acceleration off of (0, 0, 1)
    # (what it would be if the NFC was level)
    angle = np.acos(acc_dir[2])

    # TODO: Calculate angles off of a known axis, e.g. North,
    # TODO: or something set when the script is started

    print(f"Acceleration: ({acc.x:10.5f}, {acc.y:10.5f}, {acc.z:10.5f}), angle: {angle:10.5f}")
