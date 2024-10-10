import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

def get_pitch_roll_yaw():
    value = ser.readline().decode('utf-8')
    print(value)