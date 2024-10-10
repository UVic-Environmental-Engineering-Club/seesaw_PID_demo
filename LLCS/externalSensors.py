import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

def get_pitch_roll_yaw():
    try:
        value = ser.readline().decode('ascii', errors='ignore')
        print(value)
    except Exception as e:
        print(f"Error reading serial: {e}")
