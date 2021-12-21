import RPi.GPIO as GPIO
import time

BUZZER_PIN = 21

#          C    D    E    F    G    A    B    C
melody = [262, 294, 330, 349, 392, 440, 494, 523]
music = [4, 4, 5, 5, 2, 4, 2, 2, 1, 4, 4, 5, 5, 4, 4, 2, 4, 2, 1, 2, 0]
long = [6, 7, 10, 17, 18]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)

pwm.start(0)
try:
    for i in range(21):
        pwm.ChangeFrequency(melody[music[i]])
        pwm.ChangeDutyCycle(50)
        if i not in long:
            time.sleep(0.5)
            pwm.ChangeDutyCycle(0)
            time.sleep(0.05)
        elif i != 10 and i != 18:
            time.sleep(1)
            pwm.ChangeDutyCycle(0)
            time.sleep(0.05)
        else:
            time.sleep(1.5)
            pwm.ChangeDutyCycle(0)
            time.sleep(0.5)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
