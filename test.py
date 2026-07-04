from gpiozero import LED, Button
from signal import pause
from time import sleep
from random import choice

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
buttons = [button1, button2, button3, button4]

sequence = []

def all_off():
    for led in leds:
        led.off()

def flash_led(led):
    led.on()
    sleep(0.45)
    led.off()
    sleep(0.2)
    
def flash_all(times=3):
    for _ in range(times):
        for led in leds:
            led.on()
        sleep(0.25)
        all_off()
        sleep(0.25)
        
def show_sequence():
    sleep(0.8)
    for led in sequence:
        flash_led(led)
        
def wait_for_button():
    while True:
        for index, button in enumerate(buttons):
            if button.is_pressed:
                flash_led(leds[index])

                while button.is_pressed:
                    sleep(0.02)

                return leds[index]

        sleep(0.02)
        

print("Memory game started")
print("watch the LEDs, then press the buttons accordingly")

try:

    while True:

        sequence.append(choice(leds))
        print(f"Round {len(sequence)}")
        show_sequence()

        for expected_led in sequence:
            pressed_led = wait_for_button()
            if pressed_led != expected_led:
                print("Wrong!")
                print(f"Score: {len(sequence) - 1}")
                flash_all(5)
                sequence = []
                sleep(1)
                break
        else:
            print("Correct!")
            sleep(0.8)

except KeyboardInterrupt:
    print("\nStopping...")
    all_off()