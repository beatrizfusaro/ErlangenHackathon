#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# declare the GPIO-channels

channel_next = 16
channel_back = 20
channel_ok = 21


#Path to file for buttons

filepath="/var/www/html/buttons_pressed.txt"


# callbacks for GPIO-action

def button_pressed_next(channel):
    print("Next Button pressed!")
    f=open(filepath,'w')
    f.write("0")
    f.close()
    return
        
def button_pressed_back(channel):
    print("Back Button pressed!")
    f=open(filepath,'w')
    f.write("1")
    f.close()
    return    
    
def button_pressed_ok(channel):
    print("OK Button pressed!")
    f=open(filepath,'w')
    f.write("2")
    f.close()
    return

# Setting up the GPIOs

GPIO.setmode(GPIO.BCM)

GPIO.setup(channel_next, GPIO.IN)
GPIO.setup(channel_back, GPIO.IN)
GPIO.setup(channel_ok, GPIO.IN)

GPIO.add_event_detect(channel_next, GPIO.FALLING, callback=button_pressed_next, bouncetime=100)
GPIO.add_event_detect(channel_back, GPIO.FALLING, callback=button_pressed_back, bouncetime=100)
GPIO.add_event_detect(channel_ok, GPIO.FALLING, callback=button_pressed_ok, bouncetime=100)


# main loop

while True:
    
    if 1 is not 0:
        pass
    
    #if GPIO.event_detected(channel_next):
     #   print('Button pressed')
#    input_state = GPIO.input(channel_next)
#    if input_state == False:
#        print('Button Pressed')
#        time.sleep(1)

