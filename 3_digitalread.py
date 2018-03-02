import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.IN)

while 1:
    if(GPIO.input(14)==True):
        print("ON")
    if(GPIO.input(14)==False):
        print("OFF")
