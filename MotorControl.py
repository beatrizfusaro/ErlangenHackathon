import RPi.GPIO as IO
import time

class MotorControl:

    def __init__(self, radius):
        IO.setwarnings(False)          # do not show any warnings
        IO.setmode (IO.BCM)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
        IO.setup(19,IO.OUT)             # initialize GPIO19 as an output
        IO.setup(13,IO.OUT)
        self.t = IO.PMW(19, 100)
        self.s = IO.PMW(13, 100)
        t.start(5)
        s.start(5)
        IO.setup(26,IO.OUT)
        self.p = IO.PMW(26, 50)
        p.start(2.5)
        self.r = radius

    def move(self, x, y):
       angle = 180.0 * x / 3.14 / r
       duty = float(angle) / 10.0 + 2.5
       t.ChangeDutyCycle(duty)
       angle = 180.0 * y / 3.14 / r
       duty = float(angle) / 10.0 + 2.5
       s.ChangeDutyCycle(duty)
       p.ChangeDutyCycle(12.5)
       time.sleep(1)
       p.ChangeDutyCycle(2.5)
       time.sleep(0.5)
       t.ChangeDutyCycle(5)
       s.ChangeDutyCycle(5)
