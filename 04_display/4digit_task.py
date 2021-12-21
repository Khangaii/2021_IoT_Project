import RPi.GPIO as GPIO
import time

# GPIO 7개 Pin 번호 설정
#               A  B  C  D  E  F  G
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]
DIGIT_PINS = [10, 11, 12, 13]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
  GPIO.setup(segment, GPIO.OUT)
  GPIO.output(segment, GPIO.LOW)

for digit in DIGIT_PINS:
  GPIO.setup(digit, GPIO.OUT)
  GPIO.output(digit, GPIO.HIGH)

# Common Anode일 경우 : LOW -> LED ON, HIGH -> LED OFF
# Common Cathode일 경우 : LOW -> LED OFF, HIGH -> LED ON
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

def display(digit, number):
  for i in range(len(DIGIT_PINS)):
    if i+1 == digit:
      GPIO.output(DIGIT_PINS[i], GPIO.LOW)
    else:
      GPIO.output(DIGIT_PINS[i], GPIO.HIGH)
  
  for i in range(len(SEGMENT_PINS)):
    GPIO.output(SEGMENT_PINS[i], data[number][i])
  time.sleep(0.001)

try:
  pass

finally:
  GPIO.cleanup()
  print('cleanup and exit')