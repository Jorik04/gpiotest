from gpiozero import LED, Button
from signal import pause

led1 = LED(17)
led2 = LED(4)
led3 = LED(3)
led4 = LED(2)

button1 = Button(21, pull_up=True)
button2 = Button(20, pull_up=True)
button3 = Button(16, pull_up=True)
button4 = Button(9, pull_up=True)

button1.when_pressed = lambda: print("Button 1")
button2.when_pressed = lambda: print("Button 2")
button3.when_pressed = lambda: print("Button 3")
button4.when_pressed = lambda: print("Button 4")

print("Press buttons...")

leds = [led1, led2, led3, led4]

def all_off():
    for led in leds:
        led.off()

led2.on()

pause()