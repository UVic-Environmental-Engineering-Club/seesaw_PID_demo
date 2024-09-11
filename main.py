import HLCS
import LLCS
import sys
import time
#try:
#    import bluerobotics_navigator as navigator
#except ImportError:
#    raise ImportError("Bluerobotics navigaotor library was not imported\ntry: pip install bluerobotics_navigator")


def main():
    print("Hello World")
    llcs = LLCS.LLCS()
    hlcs = HLCS.HLCS()

    llcs.calibrate()
    while True:
        llcs.read_and_print_angles()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
