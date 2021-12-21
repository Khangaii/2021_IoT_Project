# pir.py
import RPi.GPIO as GPIO
import time

PIR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

time.sleep(5)
print('PIR ready...')

try:
    while True:
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:    # 1, True
            print('움직입 감지')
        else:
            print('움직임 없음')

        time.sleep(0.1)
    
finally:
    GPIO.cleanup()
    print('cleanup and exit')