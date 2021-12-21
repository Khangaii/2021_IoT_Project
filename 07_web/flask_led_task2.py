from flask import Flask, render_template
import RPi.GPIO as GPIO

RED = 4
BLUE = 3

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.output(RED, GPIO.LOW)
GPIO.output(BLUE, GPIO.LOW)

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("led2.html")

@app.route("/led/<led>/<op>")
def led_index(led, op):
  if led == "red":
    if op == "on":
      GPIO.output(RED, GPIO.HIGH)
      return "RED LED ON"
    else:
      GPIO.output(RED, GPIO.LOW)
      return "RED LED OFF"
  else:
    if op == "on":
      GPIO.output(BLUE, GPIO.HIGH)
      return "BLUE LED ON"
    else:
      GPIO.output(BLUE, GPIO.LOW)
      return "BLUE LED OFF"

if __name__ == "__main__":
  app.run(host="0.0.0.0")

GPIO.cleanup()
