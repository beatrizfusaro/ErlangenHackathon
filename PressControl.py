import RPi.GPIO as IO
import time

class PressControl:

    def __init__(self):
        IO.setwarnings(False)          # do not show any warnings
        IO.setmode (IO.BCM)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
        IO.setup(26,IO.OUT)
        self.t = IO.PMW(26, 50)
        t.start(2.5)

    def move(self):
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)
