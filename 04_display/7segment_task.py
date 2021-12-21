import RPi.GPIO as GPIO
import time

BUTTON_PIN = 4

# GPIO 7개 Pin 번호 설정
#               A  B  C  D  E  F  G
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
  GPIO.setup(segment, GPIO.OUT)
  GPIO.output(segment, GPIO.LOW)

data = [[1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1]]

try:
  pass
    
finally:
  GPIO.cleanup()
  print('cleanup and exit')