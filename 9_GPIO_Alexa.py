from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')
app.config['ASK_VERIFY_REQUESTS'] = False
@ask.intent('LocationControlIntent', mapping={'status': 'status', 'location': 'location'})
def location_control(status, location):

    locationDict = {
        'room': 4,
        'light': 2
    }

    targetPin = locationDict[location]

    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(4, GPIO.IN)
    img = ""
    if status in ['on', 'low']:
        GPIO.output(targetPin, GPIO.LOW)
    if status in ['off', 'high']:
        GPIO.output(targetPin, GPIO.HIGH)
    return statement('Turning {} {}!'.format(location, status))
