from datetime import datetime
from gpiozero import LED
from time import sleep
from threading import Thread
from signal import pause

dig_4 = LED(18)
dig_1 = LED(20)
dig_2 = LED(16)
dig_3 = LED(21)

a = LED(2)
b = LED(3)
c = LED(4)
d = LED(17)
e = LED(27)
f = LED(22)
g = LED(10)
dp = LED(9)

digits = [dig_1, dig_2, dig_3, dig_4]
segments = [a, b, c, d, e, f, g, dp]

chars = {
    '0': [1,1,1,1,1,1,0,0],
    '1': [0,1,1,0,0,0,0,0],
    '2': [1,1,0,1,1,0,1,0],
    '3': [1,1,1,1,0,0,1,0],
    '4': [0,1,1,0,0,1,1,0],
    '5': [1,0,1,1,0,1,1,0],
    '6': [1,0,1,1,1,1,1,0],
    '7': [1,1,1,0,0,0,0,0],
    '8': [1,1,1,1,1,1,1,0],
    '9': [1,1,1,1,0,1,1,0],

    'n': [0,0,1,0,1,0,1,0],
    'i': [0,1,1,0,0,0,0,0],
    'g': [1,0,1,1,1,1,1,0],
    'a': [1,1,1,0,1,1,1,0],
    ' ': [0,0,0,0,0,0,0,0],

}

display = "1234"


def all_digits_off():
    for digit in digits:
        digit.off()


def set_segments(char):
    pattern = chars.get(char.lower(), chars[' '])

    for segment, should_light in zip(segments, pattern):
        if should_light:
            segment.off()
        else:
            segment.on()


def multiplex():
    global display

    while True:
        
        display = datetime.now().strftime("%H%M")

        for digit, char in zip(digits, display):
            all_digits_off()
            set_segments(char)
            digit.on()

            sleep(0.0001)

Thread(target=multiplex, daemon=True).start()

while True:
    now = datetime.now()
    display = now.strftime("%H%M")

