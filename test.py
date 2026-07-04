from gpiozero import LED
from signal import pause

led1 = LED(17)
led2 = LED(4)
led3 = LED(3)
led4 = LED(2)

leds = [led1, led2, led3, led4]

def all_off():
	for led in leds:
		led.off()

led2.on()

pause()
