from flask import Flask
import RPi.GPIO as GPIO

RED = 4
BLUE = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)


app = Flask(__name__)


@app.route("/")
def hello_world():
  return '''
    <p>Hello, Flask!<p>
    <a href="/led/red/on">RED LED ON</a>
    <a href="/led/red/off">RED LED OFF</a> <br>
    <a href="/led/blue/on">BLUE LED ON</a>
    <a href="/led/blue/off">BLUE LED OFF</a>
  '''

@app.route("/led/<color>/<cmd>")
def led_op(color, cmd):
  print(color+cmd)
  
  if color == "red":
    if cmd == "on":
      GPIO.output(RED, GPIO.HIGH)
      return '''
        <p>RED LED ON</p>
        <a href="/">HOME</a>
      '''
    elif cmd == "off":
      GPIO.output(RED, GPIO.LOW)
      return '''
        <p>RED LED OFF<p>
        <a href="/">HOME</a>
      '''
  elif color == "blue":
    if cmd == "on":
      GPIO.output(BLUE, GPIO.HIGH)
      return '''
        <p>BLUE LED ON</p>
        <a href="/">HOME</a>
      '''
    elif cmd == "off":
      GPIO.output(BLUE, GPIO.LOW)
      return '''
        <p>BLUE LED OFF</p>
        <a href="/">HOME</a>
      '''


if __name__ == "__main__":
  app.run(host="0.0.0.0")


GPIO.cleanup()