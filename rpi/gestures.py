from apds9960.const import *
from apds9960 import APDS9960
import smbus
import keyboard
from time import sleep

port = 1
bus = smbus.SMBus(port)

apds = APDS9960(bus)

try:
    print("Gestures")
    print("============")
    
    apds.enableGestureSensor()
    while True:
        sleep(0.5)
        if apds.isGestureAvailable():
            motion = apds.readGesture()
            print("Gesture={}".format(motion))
            
            if motion == APDS9960_DIR_LEFT:
                keyboard.press_and_release('v')
            elif motion == APDS9960_DIR_RIGHT:
                keyboard.press_and_release('n')
            elif motion == APDS9960_DIR_NEAR:
                keyboard.press_and_release('b')

finally:
    print("Bye")
