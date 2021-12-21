# 7segment.py
import RPi.GPIO as GPIO
import time

# GPIO 핀 설정 (A~G)
#               A, B, C, D, E, F, G
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setmode(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

# Common Anode일 경우: LOW -> LED ON, HIGH -> LED OFF
# Common Cathode일 경우: LOW -> LED OFF, HIGH -> LED ON
#data = [0, 0, 0, 0, 0, 0, 1]
data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 0, 0, 0, 1, 1, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 1, 0, 1],  # 5
        [1, 1, 1, 1, 1, 0, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 1, 0, 1, 1]]  # 9

try:
    for _ in range(10):
        for i in range(len(SEGMENT_PINS)):      # 0~6
            GPIO.output(SEGMENT_PINS[_][i], data[_][i])

        time.sleep(1)

        for i in range(len(SEGMENT_PINS)):      # 0~6
            GPIO.output(SEGMENT_PINS[i], GPIO.LOW)

        time.sleep(1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')