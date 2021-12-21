import RPi.GPIO as GPIO
import time

RED = 2
YELLOW = 3
GREEN = 4
GPIO.setmode(GPIO.BCM)  # GPIO.BCM or GRIO.BOARD
GPIO.setup(RED, GPIO.OUT)   # GPIO.OUT or GPIO.IN
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

GPIO.output(RED, GPIO.HIGH) # 1
print("led on")
time.sleep(2)
GPIO.output(RED, GPIO.LOW) # 0
print("led off")

GPIO.output(YELLOW, GPIO.HIGH) # 1
print("led on")
time.sleep(2)
GPIO.output(YELLOW, GPIO.LOW) # 0
print("led off")

GPIO.output(GREEN, GPIO.HIGH) # 1
print("led on")
time.sleep(2)
GPIO.output(GREEN, GPIO.LOW) # 0
print("led off")

GPIO.setup(RED, GPIO.IN)
GPIO.setup(YELLOW, GPIO.IN)
GPIO.setup(GREEN, GPIO.IN)

GPIO.cleanup()  # GPIO 핀상태 초기화