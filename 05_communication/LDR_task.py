import RPi.GPIO as GPIO
import spidev
import time

LED_PIN = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# SPI 인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작
spi.open(0, 0)  # bus:0, dev:0 (CEO:0, CE1:1)

# SPI 통신 속도 설정
spi.max_speed_hz = 100000

# 0~7까지 8개의 채널에서 SPI 데이터 읽기
def analog_read(channel):
    # [byte_1, byte_2, byte_3]
    # byte_2 : channel config (channel 0) (+8) -> 0000 1000 -> 1000 0000
    ret = spi.xfer2([1,  (8 +  channel) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        ldr_value = analog_read(0)    # reading(0~1023)
        print("LDR Value: %d" % ldr_value)
        if ldr_value < 512:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.setup(LED_PIN, GPIO.IN)
    spi.close()
