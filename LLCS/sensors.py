
#! /bin/python3

import bluerobotics_navigator as navigator
import numpy as np
import math
import time

def read_and_print_angles():
    normal_x = np.array([1, 0, 0])
    normal_y = np.array([0, 1, 0])
    normal_z = np.array([0, 0, 1])

    # Get acceleration from the NFC, note that positive z is down
    acc = navigator.read_accel()

    # Normalize the acceleration vector
    acc_mag = (acc.x * acc.x + acc.y * acc.y + acc.z * acc.z) ** 0.5
    acc_dir = (acc.x / acc_mag, acc.y / acc_mag, acc.z / acc_mag)

    # Calculate acc projected to each axis plane
    acc_yz = np.linalg.norm(acc_dir - np.dot(acc_dir, normal_x) * normal_x)
    acc_xz = np.linalg.norm(acc_dir - np.dot(acc_dir, normal_y) * normal_y)
    acc_xy = np.linalg.norm(acc_dir - np.dot(acc_dir, normal_z) * normal_z)

    # Calculate angle from each axis
    angle_from_x = math.acos(- acc_yz) * 180 / math.pi
    angle_from_y = math.acos(- acc_xz) * 180 / math.pi
    angle_from_z = math.acos(- acc_xy) * 180 / math.pi

    # Use the dot product angle formula to get the angle (in radians) of acceleration off of (0, 0, 1)
    # (what it would be if the NFC was level)
    # angle = math.acos(acc_dir[2])

    # TODO: Calculate angles off of a known axis, e.g. North,
    # TODO: or something set when the script is started

    # print(f"Acceleration: ({acc.x:10.5f}, {acc.y:10.5f}, {acc.z:10.5f}), angle: {angle:10.5f}")
    print(f"acc_yz: {acc_yz:10.3f} acc_xz: {acc_xz:10.3f} acc_xy {acc_xy:10.3f}")
    print(f"angle_from_x: {angle_from_x:10.3f} angle_from_y: {angle_from_y:10.3f} angle_from_z: {angle_from_z:10.3f}")

    time.sleep(0.5)