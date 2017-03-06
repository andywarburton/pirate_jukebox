import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)

while True:
    input_state = GPIO.input(23)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)