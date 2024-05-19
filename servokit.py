import time
from adafruit_servokit import ServoKit
import servo_fun_lib
from servo_fun_lib import calib_angles
kit = ServoKit(channels=16)

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



i=0
while(i<100):
    calib_angles(60)
    #time.sleep(5)
    calib_angles(140)
    i+=1

