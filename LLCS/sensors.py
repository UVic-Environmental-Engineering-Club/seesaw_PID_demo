
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
    nfc_acc = navigator.read_accel()

    # Normalize the acceleration vector
    acc = np.array([nfc_acc.x, nfc_acc.y, nfc_acc.z])
    acc_mag = np.linalg.norm(acc)
    acc_dir = acc / acc_mag

    # Calculate acc projected to each axis plane
    # acc_yz = np.linalg.norm(acc_dir - np.dot(acc_dir, normal_x) * normal_x)
    # acc_xz = np.linalg.norm(acc_dir - np.dot(acc_dir, normal_y) * normal_y)
    # acc_xy = np.linalg.norm(acc_dir - np.dot(acc_dir, normal_z) * normal_z)

    # Calculate angle from each axis
    pitch = math.atan2(-acc_dir[0], acc_dir[2]) # math.acos(- acc_yz) * 180 / math.pi
    roll = math.atan2(acc_dir[1], acc_dir[2]) # math.acos(- acc_xz) * 180 / math.pi
    # angle_from_z = np.atan2(acc_dir[], acc_dir[]) # math.acos(- acc_xy) * 180 / math.pi

    # Use the dot product angle formula to get the angle (in radians) of acceleration off of (0, 0, 1)
    # (what it would be if the NFC was level)
    # angle = math.acos(acc_dir[2])

    # TODO: Calculate angles off of a known axis, e.g. North,
    # TODO: or something set when the script is started

    print(f"Acceleration: ({acc[0]:10.5f}, {acc[1]:10.5f}, {acc[2]:10.5f})")
    # print(f"acc_yz: {acc_yz:10.3f} acc_xz: {acc_xz:10.3f} acc_xy {acc_xy:10.3f}")
    print(f"pitch: {pitch:10.3f}, roll: {roll:10.3f}")



def get_pitch() -> float:

    # Get acceleration from the NFC, note that positive z is down
    nfc_acc = navigator.read_accel()

    # Normalize the acceleration vector
    acc = np.array([nfc_acc.x, nfc_acc.y, nfc_acc.z])
    acc_mag = np.linalg.norm(acc)
    acc_dir = acc / acc_mag
    pitch = math.atan2(-acc_dir[0], acc_dir[2])
    
    return pitch



def get_pitch_roll_yaw() -> tuple[float, float, float]:

    # Get acceleration from the NFC, note that positive z is down
    nfc_acc = navigator.read_accel()

    # Normalize the acceleration vector
    acc = np.array([nfc_acc.x, nfc_acc.y, nfc_acc.z])
    acc_mag = np.linalg.norm(acc)
    acc_dir = acc / acc_mag
    pitch = math.atan2(-acc_dir[0], acc_dir[2])
    roll = math.atan2(acc_dir[1], acc_dir[2])
    
    return (pitch, roll, 0.0)
