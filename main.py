
import sys
import time
import math
import numpy as np

import bluerobotics_navigator as navigator

import LLCS

class KalmanFilter:
    def __init__(self, process_variance, measurement_variance, estimated_measurement_variance):
        self.process_variance = process_variance
        self.measurement_variance = measurement_variance
        self.estimated_measurement_variance = estimated_measurement_variance
        self.posteri_estimate = 0.0
        self.posteri_error_estimate = 1.0

    def update(self, measurement):
        priori_estimate = self.posteri_estimate
        priori_error_estimate = self.posteri_error_estimate + self.process_variance

        blending_factor = priori_error_estimate / (priori_error_estimate + self.measurement_variance)
        self.posteri_estimate = priori_estimate + blending_factor * (measurement - priori_estimate)
        self.posteri_error_estimate = (1 - blending_factor) * priori_error_estimate

        return self.posteri_estimate



int_pitch = 0.0
int_roll = 0.0
int_yaw = 0.0
gyro_calibration = (0.0, 0.0, 0.0)
prev_time = 0.0
kalman_filter_pitch = KalmanFilter(process_variance=1e-5, measurement_variance=1e-1, estimated_measurement_variance=1e-1)
kalman_filter_roll = KalmanFilter(process_variance=1e-5, measurement_variance=1e-1, estimated_measurement_variance=1e-1)


def testing_loop(print_info = False):
    global int_pitch
    global int_roll
    global int_yaw
    global prev_time

    (pitch, roll, yaw) = LLCS.sensors.get_pitch_roll_yaw()
    ang_vel = navigator.read_gyro()

    if math.isnan(ang_vel.x) or math.isnan(ang_vel.y) or math.isnan(ang_vel.z) or math.isnan(pitch) or math.isnan(roll) or math.isnan(yaw)\
        or (pitch == 0.0 and roll == 0.0 and yaw == 0.0):
        return

    next_time = time.time()
    time_delta = (next_time - prev_time)# / 1_000_000_000
    prev_time = next_time

    int_pitch += (ang_vel.y - gyro_calibration[1]) * time_delta
    int_roll += (ang_vel.x - gyro_calibration[0]) * time_delta
    int_yaw += -(ang_vel.z - gyro_calibration[2]) * time_delta

    # Update Kalman filters
    filtered_pitch = kalman_filter_pitch.update(int_pitch)
    filtered_roll = kalman_filter_roll.update(int_roll)

    if not print_info:
        return

    pitch_error = pitch - int_pitch
    roll_error = roll - int_roll
    yaw_error = yaw - int_yaw

    print(f"Last Delta: {time_delta:1.7f}, Error: ({pitch_error:1.5f} ({(15.9154943092 * pitch_error):3.2f}%), {roll_error:1.5f} ({(15.9154943092 * roll_error):3.2f}%)), Integrated: ({int_pitch:1.5f}, {int_roll:1.5f}), Actual: ({pitch:1.5f}, {roll:1.5f})")



def calibrate():
    global gyro_calibration

    print("Calibrating, keep still")

    num_iter = 10_000
    readings = []

    for _ in range(num_iter):
        ang_vel = navigator.read_gyro()
        readings.append((ang_vel.x, ang_vel.y, ang_vel.z))
        time.sleep(0.001)  # Add a small delay to ensure stability

    # Convert to numpy array for easier manipulation
    readings = np.array(readings)

    # Calculate mean and standard deviation
    mean = np.mean(readings, axis=0)
    std_dev = np.std(readings, axis=0)

    # Discard outliers (values more than 2 standard deviations from the mean)
    filtered_readings = readings[
        (np.abs(readings - mean) < 2 * std_dev).all(axis=1)
    ]

    # Calculate the average of the filtered readings
    gyro_calibration_x, gyro_calibration_y, gyro_calibration_z = np.mean(filtered_readings, axis=0)
    gyro_calibration = (gyro_calibration_x, gyro_calibration_y, gyro_calibration_z)

    # Calculate variance
    variance = np.var(filtered_readings, axis=0)

    input(f"Done still calibration, values: ({gyro_calibration[0]}, {gyro_calibration[1]}, {gyro_calibration[2]}). Press enter to continue")

    return variance



def main():
    global int_pitch
    global int_roll
    global int_yaw
    global prev_time
    global gyro_calibration
    global kalman_filter_pitch
    global kalman_filter_roll

    navigator.init()

    (int_pitch, int_roll, int_yaw) = LLCS.sensors.get_pitch_roll_yaw()

    variance = calibrate()
    
    prev_time = time.time()

    # Use the variance to set the Kalman filter parameters
    process_variance = 1e-5  # This can be tuned further
    measurement_variance_pitch = variance[1]  # Variance of y-axis for pitch
    measurement_variance_roll = variance[0]  # Variance of x-axis for roll

    kalman_filter_pitch = KalmanFilter(process_variance, measurement_variance_pitch, measurement_variance_pitch)
    kalman_filter_roll = KalmanFilter(process_variance, measurement_variance_roll, measurement_variance_roll)


    try:
        i = 0
        while True:
            testing_loop(i % 1_000 == 0)
            i += 1
    finally:
        print("Done")



if __name__ == "__main__":
    main()
