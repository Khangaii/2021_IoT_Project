from typing import Text
import RPi.GPIO as GPIO

RED = 2
YELLOW = 3
GREEN = 4
BUTTON_RED = 9
BUTTON_YELLOW = 10
BUTTON_GREEN = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BUTTON_RED, GPIO.IN)
GPIO.setup(BUTTON_YELLOW, GPIO.IN)
GPIO.setup(BUTTON_GREEN, GPIO.IN)

red_on = False
yellow_on = False
green_on = False

try:
    while True:
        red = GPIO.input(BUTTON_RED)
        yellow = GPIO.input(BUTTON_YELLOW)
        green = GPIO.input(BUTTON_GREEN)
        if not red_on and red == GPIO.HIGH:
            GPIO.output(RED, GPIO.HIGH)
            red_on = True
        elif red_on and red == GPIO.LOW:
            GPIO.output(RED, GPIO.LOW)
            red_on = False
        if not yellow_on and yellow == GPIO.HIGH:
            GPIO.output(YELLOW, GPIO.HIGH)
            yellow_on = True
        elif yellow_on and yellow == GPIO.LOW:
            GPIO.output(YELLOW, GPIO.LOW)
            yellow_on = False
        if not green_on and green == GPIO.HIGH:
            GPIO.output(GREEN, GPIO.HIGH)
            green_on = True
        elif green_on and green == GPIO.LOW:
            GPIO.output(GREEN, GPIO.LOW)
            green_on = False
finally:
    GPIO.cleanup()
    print('cleanup and exit')
        