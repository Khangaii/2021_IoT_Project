import RPi.GPIO as GPIO
import time

# GPIO 7개 Pin 번호 설정
#               A  B  C  D  E  F  G
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
  GPIO.setup(segment, GPIO.OUT)
  GPIO.output(segment, GPIO.LOW)

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

try:
  for i in range(10):
    for j in range(len(SEGMENT_PINS)):
      GPIO.output(SEGMENT_PINS[j], data[i][j])

    time.sleep(1)
    
finally:
  GPIO.cleanup()
  print('cleanup and exit')