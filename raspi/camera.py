#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()

camera.start_preview()
sleep(1)
camera.capture('/home/pi/image_{:%Y-%m-%d_%H:%M:%S}.jpg'.format(datetime.datetime.now()))
camera.stop_preview()

