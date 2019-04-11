"Program to make one cozmo draw/mark works by splitting them up into individual letters"

import cozmo
import socket
import errno
from socket import error as socket_error

# need to get movement info
from cozmo import robot
from cozmo.util import degrees, distance_mm, speed_mmps
"""
segment = 203.2
space = 100
class cozmoAlphabet:
    instructions = []


    def letterA(robot: cozmo.robot.Robot):
        robot.set_lift_height(0, 25).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(segment),
                             cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(segment),
                             cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm((segment / 2)), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm((-segment)), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm((segment / 2)), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.set_lift_height(1, 25).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()

        print('I am ready for next letter')
    def letterB(robot: cozmo.robot.Robot):
        robot.set_lift_height(0, 25).wait_for_completed()#drop marker to ground
        robot.drive_straight(cozmo.util.distance_mm(segment),cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm((segment/2)), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.set_lift_height(1, 25).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm((-segment)), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.set_lift_height(0, 25).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm((segment / 2)), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.set_lift_height(1, 25).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
        print('I am ready for next letter')

        
    def letterC(robot: cozmo.robot.Robot):
        robot.set_lift_height(0, 25).wait_for_completed()  # drop marker to ground
        robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.set_lift_height(1, 25).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
        robot.set_lift_height(0, 25).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.set_lift_height(1, 25).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(-segment), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
        print('I am ready for next letter')"""
print("yeyeyey")
print("test test test")
inch = 25.4
doubleInche = 51.0 #distance to move after raising lift before end of one line to adjust for turn
reverseDist = 35.0
segment = 203.2
#BEFORE any turns


def raiseTurn(direction, robot: cozmo.robot.Robot ):
    if direction == "L":
        robot.set_lift_height(1, 15).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()  # turn left
        robot.drive_straight(cozmo.util.distance_mm(-(reverseDist)),cozmo.util.speed_mmps(200)).wait_for_completed()
        robot.set_lift_height(0, 15).wait_for_completed()
        robot.drive_straight(cozmo.util.distance_mm(reverseDist), cozmo.util.speed_mmps(200)).wait_for_completed()
    elif direction == "R":
        print("this is before raise")
        robot.set_lift_height(1, 15).wait_for_completed()
        print("this is after raise")
        print("before turn")
        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()  # turn right
        print("after turn")
        print("before reversing reverseDist")
        robot.drive_straight(cozmo.util.distance_mm(-(reverseDist)), cozmo.util.speed_mmps(200)).wait_for_completed()
        print("after reversing reverseDist")
        print("before dropping lift")
        robot.set_lift_height(0, 15).wait_for_completed()
        print("after dropping lift")
        print("before driving straight the reverseDist")
        robot.drive_straight(cozmo.util.distance_mm(reverseDist), cozmo.util.speed_mmps(200)).wait_for_completed()
        print("after driving straight the reverseDist")
    else:
        print ("Not a valid input for direction argument")


def preTurn(robot: cozmo.robot.Robot):
    robot.set_lift_height(1, 15).wait_for_completed()
    robot.drive_straight(cozmo.util.distance_mm(doubleInche), cozmo.util.speed_mmps(125)).wait_for_completed()

#Functions to simply raise or drop the lift (saves some typing)
def raiseLift(robot: cozmo.robot.Robot):
    robot.set_lift_height(1,15).wait_for_completed()
def dropLift(robot: cozmo.robot.Robot):
    robot.set_lift_height(0,15).wait_for_completed\
        ()

# Driving in a straight line
# argument "dist_mm" should be positive if forward movement is desired, and negative otherwise.
def driveStraight(dist_mm, robot: cozmo.robot.Robot):
    robot.drive_straight(cozmo.util.distance_mm(dist_mm), cozmo.util.speed_mmps(125)).wait_for_completed()

def cozmoAlphabet(robot: cozmo.robot.Robot):

    instructions = 'A'
    alphabetList = []
    print('yes')
    alphabetList.append(instructions)
    print('no')
    #segment = 203.2
    space = 100
    left = 'L' #90
    right = 'R'#-90
    print(alphabetList)
    for letter in alphabetList:
        if letter == 'A':
            robot.drive_straight(cozmo.util.distance_mm(-reverseDist), cozmo.util.speed_mmps(125)).wait_for_completed()
            robot.set_lift_height(0, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(125)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(doubleInche), cozmo.util.speed_mmps(125)).wait_for_completed()

            raiseTurn("R",robot)
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(125)).wait_for_completed()

            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(doubleInche), cozmo.util.speed_mmps(125)).wait_for_completed()
            raiseTurn("R",robot)
            robot.drive_straight(cozmo.util.distance_mm((segment / 3)), cozmo.util.speed_mmps(125)).wait_for_completed()

            robot.set_lift_height(1, 15).wait_for_completed()
            raiseTurn("R",robot)
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(125)).wait_for_completed()

            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm((-segment - reverseDist)),
                                 cozmo.util.speed_mmps(125)).wait_for_completed()

            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(doubleInche), cozmo.util.speed_mmps(125)).wait_for_completed()

            raiseTurn("L",robot)
            robot.drive_straight(cozmo.util.distance_mm((segment - segment / 2)),cozmo.util.speed_mmps(125)).wait_for_completed()

            robot.set_lift_height(1, 15).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()  # turns right
            robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(125)).wait_for_completed()

            raiseTurn("L", robot)
            print('I drew A and am ready for next letter')
        if letter == 'B':
            robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            raiseTurn("R", robot)#turns right
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            raiseTurn("R", robot)#turns right
            robot.drive_straight(cozmo.util.distance_mm((segment / 2)),cozmo.util.speed_mmps(200)).wait_for_completed()
            raiseTurn("R", robot)
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm((-segment)),cozmo.util.speed_mmps(200)).wait_for_completed()
            raiseTurn("L", robot)#turns left
            robot.set_lift_height(0, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm((segment / 2)),cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
            print('I drew B and am ready for next letter')
        if letter == 'C':
            robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()#turn right
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()  #Raise marker
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
            robot.set_lift_height(0, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(-segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(180), in_parallel=True).wait_for_completed()#turn to face other side
            robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()#turn left
            print('I drew C and am ready for next letter')
        if letter == 'D':
            robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(-(segment/8)), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(0, 15).wait_for_completed()# drop marker to ground
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()  # turn right
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()  # turn right
            robot.drive_straight(cozmo.util.distance_mm(segment-15), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(-segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()#turn left
            robot.drive_straight(cozmo.util.distance_mm(15), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()  # turn left
            robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
        if letter == 'E':
            #need to reverse cozmo 2.25 inches after every turn == 57.15 mm
            robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()  # Raise marker
            robot.drive_straight(cozmo.util.distance_mm(-segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(-(segment/2)), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(segment/2),cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()  # drop marker to ground
            robot.drive_straight(cozmo.util.distance_mm(-(segment / 2)), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(-(segment/2)), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(segment),cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()  # drop marker to ground
            robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()

        """ THIS IS AFTER IMPLEMENTATION OF REVERSEDIST"""
        if letter == 'F':
            # Setup and drop Lift
            robot.drive_straight(cozmo.util.distance_mm(-reverseDist), cozmo.util.speed_mmps(125)).wait_for_completed()
            robot.set_lift_height(0, 15).wait_for_completed()
            # Drive forward one full segment (Left vertical component of F
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(125)).wait_for_completed()
            # Preturn adjustmennts (call preTurn function)
            preTurn(robot)
            #turn right to tackle the high-horizontal component of F
            raiseTurn("R", robot)
            dropLift(robot)  # ready to draw
            driveStraight(segment)
            ##CONTINUE HERE.







print("ththth")
cozmo.run_program(cozmoAlphabet)