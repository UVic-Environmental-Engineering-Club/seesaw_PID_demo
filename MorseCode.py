
#! /bin/python3

import bluerobotics_navigator as brn
import time
import sys




# Char to Morse code map. 1 is dash, 0 is dot
morse_code: dict = {
    'a': "01",
    'b': "1000",
    'c': "1010",
    'd': "100",
    'e': "0",
    'f': "0010",
    'g': "110",
    'h': "0000",
    'i': "00",
    'j': "0111",
    'k': "101",
    'l': "0100",
    'm': "11",
    'n': "10",
    'o': "111",
    'p': "0110",
    'q': "1101",
    'r': "010",
    's': "000",
    't': "1",
    'u': "001",
    'v': "0001",
    'w': "011",
    'x': "1001",
    'y': "1011",
    'z': "1100",
    '1': "01111",
    '2': "00111",
    '3': "00011",
    '4': "00001",
    '5': "00000",
    '6': "10000",
    '7': "11000",
    '8': "11100",
    '9': "11110",
    '0': "11111"
}




def write_letter(letter: str, unit: float) -> None:

    code = morse_code.get(letter.lower()[0], "0")

    for dit in code:
        print(f"Writing {dit}")
        brn.set_led(brn.UserLed.Led1, True)

        if dit == '0':
            # Dot is one unit
            time.sleep(unit)
        else:
            # Dash is three units
            time.sleep(3.0 * unit)

        brn.set_led(brn.UserLed.Led1, False)

        # Time between dits is one unit
        time.sleep(unit)




def write_message(message: str, unit: float = 0.2) -> None:

    words = message.lower().split(' ')

    for word in words:
        for letter in word:
            # Only look at alpha numeric chars
            if not letter.isalnum():
                continue

            print(f"Writing {letter}")
            write_letter(letter, unit)

            # Three units between letters, write letter adds an extra unit at the end
            time.sleep(2.0 * unit)
        
        # Total of seven units between words
        time.sleep(4.0 * unit)




if __name__ == "__main__":

    brn.init()

    message = "Happy Birthday Michael!"

    if len(sys.argv) > 1:
        last_arg = sys.argv[-1]
        if isinstance(last_arg, str):
            message = last_arg

    write_message(message)
