import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
print("Initializing ServoKit")

leg_front_left = [1, 3, 5]
leg_front_right = [2, 4, 6]
leg_back_left = [15, 13, 11]
leg_back_right = [14, 12, 10]

# 3 servos in leg, so 3 different degs
def leg_move(leg, degs):
    i = 1
    for servo_nb in leg:
        kit.servo[servo_nb].angle = degs[i]
        i+=1

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

i=0
while(i<100):
    all_movement(80)
    #time.sleep(5)
    all_movement(120)
    i+=1

