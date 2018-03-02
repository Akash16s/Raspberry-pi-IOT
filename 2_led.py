import time
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setmode(GPIO.BCM)      ## Use board pin numbering
GPIO.setup(2,GPIO.OUT)      ## Setup GPIO Pin 2 to OUT
GPIO.setwarnings(False)
while True:
	GPIO.output(2,True)  ##Turn on Led
	print('on')
	time.sleep(1)         ## Wait for one second
	GPIO.output(2,False) ## Turn off Led
	print('off')
	time.sleep(1)         ## Wait for one second
