import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def calib_angles(a):
    #left front leg
    kit.servo[1].angle = a
    kit.servo[3].angle = a
    kit.servo[5].angle = a
    time.sleep(1)
    #right front leg
    kit.servo[2].angle = a
    kit.servo[4].angle = a
    kit.servo[6].angle = a
    time.sleep(1)
    #left back leg
    kit.servo[15].angle = a
    kit.servo[13].angle = a
    kit.servo[11].angle = a
    time.sleep(1)
    #right back leg
    kit.servo[14].angle = a
    kit.servo[12].angle = a
    kit.servo[10].angle = a
    time.sleep(1)

def rest_mode(a):
    #left front leg
    kit.servo[1].angle = 15
    kit.servo[3].angle = 100
    kit.servo[5].angle = 45
    time.sleep(1)
    #right front leg
    kit.servo[2].angle = a
    kit.servo[4].angle = 80
    kit.servo[6].angle = 135
    time.sleep(1)
    #left back leg
    kit.servo[15].angle = 0
    kit.servo[13].angle = 100
    kit.servo[11].angle = 40
    time.sleep(1)
    #right back leg
    kit.servo[14].angle = a
    kit.servo[12].angle = 80
    kit.servo[10].angle = 135
    time.sleep(1)

def get_up(a):
    #shoulders
    kit.servo[5].angle = 110
    kit.servo[6].angle = 90
    kit.servo[10].angle = 90
    kit.servo[11].angle = 90
    time.sleep(1)
    #forearms
    kit.servo[3].angle = 45
    kit.servo[4].angle = 135
    kit.servo[13].angle = 40
    kit.servo[12].angle = 135
    time.sleep(1)
    #arms
    kit.servo[1].angle = 70
    kit.servo[2].angle = a
    kit.servo[15].angle = 55
    kit.servo[14].angle = a
    time.sleep(1)

def lie_down(a):
    #arms
    kit.servo[1].angle = 15
    kit.servo[2].angle = a
    kit.servo[15].angle = 0
    kit.servo[14].angle = a
    time.sleep(1)
    #forearms
    kit.servo[3].angle = 100
    kit.servo[4].angle = 80
    kit.servo[13].angle = 100
    kit.servo[12].angle = 80
    time.sleep(1)
    #shoulders
    kit.servo[5].angle = 45
    kit.servo[6].angle = 135
    kit.servo[10].angle = 135
    kit.servo[11].angle = 40
