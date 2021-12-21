from lcd import drivers
import Adafruit_DHT
import time
import datetime


display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
    print("Writing to display")
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            now = datetime.datetime.now()
            print(now.strftime("%x %X"))
            print('Temperature=%.1f* Humidity=%.1f%%' % (t, h))
            display.lcd_display_string(now.strftime("%x%X"), 1)
            display.lcd_display_string("%.1f*, %.1f%%" % (t, h), 2)
            time.sleep(1)
        else:
            print('Read Error')
finally:
    print("Cleaning up!")
    display.lcd_clear()