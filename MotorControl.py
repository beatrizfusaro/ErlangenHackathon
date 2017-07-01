#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

step_size = 0.1
step_time = 0.01

class MotorControl:

    def __init__(self):
        GPIO.setwarnings(False)             # do not show any warnings
        GPIO.setmode (GPIO.BCM) 
                                            # programming the GPGPIO by BCM pin numbers. (like PIN29 as‘GPGPIO5’)
        GPIO.setup(19,GPIO.OUT)             # initialize GPGPIO19 as an output
        GPIO.setup(13,GPIO.OUT)
        GPIO.setup(26,GPIO.OUT)
        
        self.t = GPIO.PWM(19, 100)
        self.s = GPIO.PWM(13, 100)
        self.p = GPIO.PWM(26, 50)
        
        self.dutycycle_t = 5
        self.dutycycle_s = 5
        self.dutycycle_p = 5
        
        self.t.start(self.dutycycle_t)
        self.s.start(self.dutycycle_s)
        self.p.start(self.dutycycle_p)

    def cleanup_servos(self):
        self.update_dutycycles_s_t(5, 5)
        
    def update_dutycycles_s_t(self, new_dc_s, new_dc_t):
        
        while (self.dutycycle_s != new_dc_s or self.dutycycle_t != new_dc_t):
            
            #if block for channel s
            
            if self.dutycycle_s == new_dc_s:
                pass
            elif abs(self.dutycycle_s - new_dc_s) <= step_size:
               self.dutycycle_s = new_dc_s
               #print ("case 1 s")
            elif self.dutycycle_s < new_dc_s:
                self.dutycycle_s += step_size
                #print("case 2 s")
            elif self.dutycycle_s > new_dc_s:
                self.dutycycle_s -= step_size
                #print("case 3 s")
            else:
                print("Something wrong with s")
            
            #if block for channel t
            
            if self.dutycycle_t == new_dc_t:
                pass
            elif abs(self.dutycycle_t - new_dc_t) <= step_size:
               self.dutycycle_t = new_dc_t
               #print ("case 1 t")
            elif self.dutycycle_t < new_dc_t:
                self.dutycycle_t += step_size
                #print("case 2 t")
            elif self.dutycycle_t > new_dc_t:
                self.dutycycle_t -= step_size
                #print("case 3 t")
            else:
                print("Something wrong with t")
            
            self.s.ChangeDutyCycle(self.dutycycle_s)
            self.t.ChangeDutyCycle(self.dutycycle_t)
            
            time.sleep(step_time)
        

    def move(self, x, y): #max x and y = 3.14 each
        angle = 180.0 * x / (3.14)
        print ("Angle X: " +str(angle))
        if angle > 180:
            duty_t = 180 / 10.0 + 2.5
            print("Duty X: " + str(duty_t))
        else
            duty_t = float(angle) / 10.0 + 2.5
            print("Duty X: " + str(duty_t))

        angle = 180.0 * y / 3.14 
        print ("Angle Y: " +str(angle))
        if angle > 180:
            duty_s = 180 / 10.0 + 2.5
            print("Duty X: " + str(duty_t))
        else
            duty_s = float(angle) / 10.0 + 2.5
            print("Duty X: " + str(duty_t))

       
        self.update_dutycycles_s_t(duty_s, duty_t)
       
    def press(self):
        self.p.ChangeDutyCycle(12.5)
        time.sleep(1)
        self.p.ChangeDutyCycle(2.5)
        time.sleep(0.5)
       
    
servo_1 = MotorControl(1)

time.sleep(1)

servo_1.move(1, 1)
#
time.sleep(1)

servo_1.move(3, 3)

servo_1.cleanup_servos()

