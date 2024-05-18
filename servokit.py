import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
print("Initializing ServoKit")
i=0

def all_movement(a):
    #left front leg
    kit.servo[1].angle = a
    kit.servo[3].angle = a
    kit.servo[5].angle = a
    time.sleep(2)
    #right front leg
    kit.servo[2].angle = a
    kit.servo[4].angle = a
    kit.servo[6].angle = a
    time.sleep(2)
    #left back leg
    kit.servo[15].angle = a
    kit.servo[13].angle = a
    kit.servo[11].angle = a
    time.sleep(2)
    #right back leg
    kit.servo[14].angle = a
    kit.servo[12].angle = a
    kit.servo[10].angle = a
    time.sleep(2)


while(i<100):
    all_movement(80)
    #time.sleep(5)
    all_movement(120)
    i+=1

