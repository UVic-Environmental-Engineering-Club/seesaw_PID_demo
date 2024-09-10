import HLCS
import LLCS
import sys
#try:
#    import bluerobotics_navigator as navigator
#except ImportError:
#    raise ImportError("Bluerobotics navigaotor library was not imported\ntry: pip install bluerobotics_navigator")


def main():
    print("Hello World")
    llcs = LLCS.LLCS()
    hlcs = HLCS.HLCS()

    llcs.calibrate()
    llcs.read_and_print_angles()

if __name__ == "__main__":
    main()
