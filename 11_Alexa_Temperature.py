from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 17
GPIO.setmode(GPIO.BCM)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

app = Flask(__name__)
ask = Ask(app, '/')
app.config['ASK_VERIFY_REQUESTS'] = False
@ask.intent('LocationControlIntent', mapping={'status': 'status', 'location': 'location'})
def location_control(status, location):

    locationDict = {
        'room': 17,
        'light': 2
    }

    targetPin = locationDict[location]

    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(4, GPIO.IN)
    img = ""
    if status in ['on', 'low']:
        img = "https://upload.wikimedia.org/wikipedia/commons/1/14/Incandescent_light_bulb_on_db.jpg"
        GPIO.output(targetPin, GPIO.LOW)
    if status in ['off', 'high']:
        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Bulbgraph_Off.svg/2000px-Bulbgraph_Off.svg.png"
        GPIO.output(targetPin, GPIO.HIGH)
    if status in ['temperature', 'status']:
        if humidity is not None and temperature is not None:
            return('The temperature is {0:0.1f}*. And the Humidity is {1:0.1f}%'.format(temperature, humidity))
        else:
            return('Failed to get the temperature. Try again!')
    return statement('Turning {} {}!'.format(location, status)) \
           .standard_card(title="The Light changed to {}.".format(status), text="The light is now {}.".format(status), small_image_url=img, large_image_url=img)
