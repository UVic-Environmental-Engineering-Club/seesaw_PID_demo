import serial

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

def get_pitch_roll_yaw():
    try:
        value = ser.readline().decode('utf-8', errors='ignore')
        if value:
            print(value)
        else:
            print("No value received within timeout")
    except Exception as e:
        print(f"Error reading serial: {e}")
