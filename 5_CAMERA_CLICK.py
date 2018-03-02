from picamera import PiCamera
from time import sleep

camera = PiCamera()
sleep(1)
camera.start_preview()
print("Clicking picture")
camera.capture('/home/pi/Desktop/image.jpg')
sleep(0.1)
camera.stop_preview()
