import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
print("Initializing ServoKit")
i=0
while(i<100):
    #kit.servo[0].angle = 90
    #Kit.servo[1].angle = 90
    #kit.servo[4].angle = 90
    kit.servo[5].angle = 60
    time.sleep(3)
    #kit.servo[0].angle = 120
    #kit.servo[1].angle = 110
    #kit.servo[4].angle = 140
    kit.servo[5].angle = 140
    time.sleep(3)
    i+=1