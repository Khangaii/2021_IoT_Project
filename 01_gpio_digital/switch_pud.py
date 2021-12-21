import RPi.GPIO as GPIO
import time

SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
#다운저항
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#풀저항
#GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    printf("cleanup and exit")
    