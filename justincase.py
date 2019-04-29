"Program to make one cozmo draw/mark works by splitting them up into individual letters"

import cozmo
import math  # we'll need this for square roots.
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
doubleInche = 51.0  # distance to move after raising lift before end of one line to adjust for turn
reverseDist = 35.0
segment = 203.2


# BEFORE any turns


def raiseTurn(direction, robot: cozmo.robot.Robot):
    if direction == "L":
        robot.set_lift_height(1, 15).wait_for_completed()
        robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()  # turn left
        robot.drive_straight(cozmo.util.distance_mm(-reverseDist), cozmo.util.speed_mmps(200)).wait_for_completed()
        # *********************************************************************************************************
        # robot.set_lift_height(0, 15).wait_for_completed()  # This may not work in every instance we need to turn
        # *********************************************************************************************************
        robot.drive_straight(cozmo.util.distance_mm(reverseDist), cozmo.util.speed_mmps(200)).wait_for_completed()
    elif direction == "R":
        print("this is before raise")
        robot.set_lift_height(1, 15).wait_for_completed()
        print("this is after raise")
        print("before turn")
        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()  # turn right
        print("after turn")
        print("before reversing reverseDist")
        robot.drive_straight(cozmo.util.distance_mm(-reverseDist), cozmo.util.speed_mmps(200)).wait_for_completed()
        print("after reversing reverseDist")
        print("before dropping lift")
        # robot.set_lift_height(0, 15).wait_for_completed()
        print("after dropping lift")
        print("before driving straight the reverseDist")
        robot.drive_straight(cozmo.util.distance_mm(reverseDist), cozmo.util.speed_mmps(200)).wait_for_completed()
        print("after driving straight the reverseDist")
    else:
        print("Not a valid input for direction argument")


def preTurn(robot: cozmo.robot.Robot):
    robot.set_lift_height(1, 15).wait_for_completed()  # lift comes up
    robot.drive_straight(cozmo.util.distance_mm(doubleInche), cozmo.util.speed_mmps(125)).wait_for_completed()


# Functions to simply raise or drop the lift (saves some typing)
def raiseLift(robot: cozmo.robot.Robot):
    robot.set_lift_height(1, 15).wait_for_completed()


def dropLift(robot: cozmo.robot.Robot):
    robot.set_lift_height(0, 15).wait_for_completed \
        ()


# Driving in a straight line
# argument "dist_mm" should be positive if forward movement is desired, and negative otherwise.
def driveStraight(dist_mm, robot: cozmo.robot.Robot):
    robot.drive_straight(cozmo.util.distance_mm(dist_mm), cozmo.util.speed_mmps(125)).wait_for_completed()


def raiseTurnL45(robot):
    raiseLift(robot)
    robot.turn_in_place(cozmo.util.degrees(45), in_parallel=True).wait_for_completed()
    driveStraight(-reverseDist, robot)
    dropLift(robot)
    driveStraight(reverseDist, robot)


def raiseTurnR45(robot):
    raiseLift(robot)
    robot.turn_in_place(cozmo.util.degrees(-45), in_parallel=True).wait_for_completed()
    driveStraight(-reverseDist, robot)
    dropLift(robot)
    driveStraight(reverseDist, robot)


def raiseTurnL135(robot):
    raiseLift(robot)
    robot.turn_in_place(cozmo.util.degrees(135), in_parallel=True).wait_for_completed()
    driveStraight(-reverseDist, robot)
    dropLift(robot)
    driveStraight(reverseDist, robot)


def raiseTurnR135(robot):
    raiseLift(robot)
    robot.turn_in_place(cozmo.util.degrees(-135), in_parallel=True).wait_for_completed()
    driveStraight(-reverseDist, robot)
    dropLift(robot)
    driveStraight(reverseDist, robot)


def raiseTurnR157(robot):
    raiseLift(robot)
    robot.turn_in_place(cozmo.util.degrees(-157.4), in_parallel=True).wait_for_completed()
    driveStraight(-reverseDist, robot)
    dropLift(robot)
    driveStraight(reverseDist, robot)


def raiseTurnL157(robot):
    raiseLift(robot)
    robot.turn_in_place(cozmo.util.degrees(157.4), in_parallel=True).wait_for_completed()
    driveStraight(-reverseDist, robot)
    dropLift(robot)
    driveStraight(reverseDist, robot)


def raiseTurnL20(robot):
    robot.turn_in_place(cozmo.util.degrees(20), in_parallel=True).wait_for_completed()
    # driveStraight(-reverseDist, robot)


def cozmoAlphabet(robot: cozmo.robot.Robot):
    instructions = 'K'
    alphabetList = []
    print('yes')
    alphabetList.append(instructions)
    print('no')
    # segment = 203.2
    space = 100
    left = 'L'  # 90
    right = 'R'  # -90
    print(alphabetList)
    for letter in alphabetList:
        if letter == 'A':
            """
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
            print('I drew A and am ready for next letter')"""

            # ^ ^ ^ ^ We got the above to work ^ ^ ^ ^
            # checking to see if it'll work in our shorthand too.
            # This is for letter A

            driveStraight(-reverseDist, robot)
            dropLift(robot)
            driveStraight(segment, robot)  # draw the left vertical component of A
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # Draw the topmost horizontal component of A
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)  # draw upperhalf of the right vertical segment of A
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # draw lower horizontal component of A
            raiseLift(robot)
            driveStraight(-segment, robot)  # reverse course
            preTurn(robot)
            raiseTurn("L", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)  # Draw the lower half of the right vertical component of A
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(space, robot)  # move to the start-point of next letter
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - needs to be reviewed/tested. -AC, 4/14
        if letter == 'B':
            robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            raiseTurn("R", robot)  # turns right
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            raiseTurn("R", robot)  # turns right
            robot.drive_straight(cozmo.util.distance_mm((segment / 2)), cozmo.util.speed_mmps(200)).wait_for_completed()
            raiseTurn("R", robot)
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm((-segment)), cozmo.util.speed_mmps(200)).wait_for_completed()
            raiseTurn("L", robot)  # turns left
            robot.set_lift_height(0, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm((segment / 2)), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
            print('I drew B and am ready for next letter')
        if letter == 'C':
            """robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
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
            print('I drew C and am ready for next letter')"""

            # This is for C
            driveStraight(-reverseDist, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # bottom horizontal section of C
            raiseLift(robot)
            driveStraight(-segment, robot)  # go back to init
            preTurn(robot)
            raiseTurn("L", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # left vertical section of C
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # top horizontal section of C
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment, robot)  # get down to bottom right corner
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(space, robot)  # get ready to write the next letter after left turn
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - needs to be tested/reviewed.  - AC, 4/13

        if letter == 'D':
            robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(-(segment / 8)),
                                 cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(0, 15).wait_for_completed()  # drop marker to ground
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()  # turn right
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()  # turn right
            robot.drive_straight(cozmo.util.distance_mm(segment - 15), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(-90), in_parallel=True).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.set_lift_height(1, 15).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(-segment), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()  # turn left
            robot.drive_straight(cozmo.util.distance_mm(15), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()  # turn left
            robot.drive_straight(cozmo.util.distance_mm(space), cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()
        if letter == 'E':
            """"#need to reverse cozmo 2.25 inches after every turn == 57.15 mm
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
            robot.turn_in_place(cozmo.util.degrees(90), in_parallel=True).wait_for_completed()"""

            # This is for E.
            driveStraight(-reverseDist, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # bottom-most horizontal component
            raiseLift(robot)
            driveStraight(-segment, robot)  # reverse to init, turn left
            preTurn(robot)
            raiseTurn("L", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)  # draw the lower half of E's vertical component
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)  # draw middle horizontal part of E
            raiseLift(robot)
            driveStraight(-segment / 2, robot)  # reverse back to left hand side, turn left
            preTurn(robot)
            raiseTurn("L", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)  # draw the upper half of E's vertical component.
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # draw the topmost horizontal component of E
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment, robot)  # moving to bottom right corner
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - Needs to be tested/reviewed.  -AC, 4/14

        """   A, B, C, D, E all need to be fixed yet."""
        if letter == 'F':
            # Setup and drop Lift
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            # Drive forward one full segment (Left vertical component of F
            driveStraight(segment, robot)
            # Preturn adjustments (call preTurn function)
            preTurn(robot)
            # turn right to tackle the high-horizontal component of F
            raiseTurn("R", robot)
            dropLift(robot)  # ready to draw
            driveStraight(segment, robot)  # top horizontal line completed
            # preTurn, turn right, and drive down 1/2 of a segment to get to middle-height of the right side of F
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment / 2, robot)
            # now we turn right, move forward another half of a segment before we can start drawing the middle horizontal line of F
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment / 2, robot)
            # now we'r ready to draw that line (1/2 segment long)
            dropLift(robot)
            driveStraight(segment / 2, robot)
            # turn left and drive down to where we started, before driving over to the next ready position
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment + space, robot)
            # turn left to get to next ready position and we're done.
            preTurn(robot)
            raiseTurn("L", robot)
            # F is done and ready to be reviewed. - AC
        # Remind me to ask you about string input vs. list input.
        if letter == "G":
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight((3 / 4) * segment, robot)
            dropLift(robot)
            driveStraight((1 / 4) * segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight((1 / 4) * segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment / 2, robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment / 4, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done, will need to be reviewed/tested -AC, 4/11

        if letter == "H":
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)
            raiseLift(robot)
            driveStraight(-segment, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done, needs to be reviewed/tested - AC, 4/11

        if letter == "I":
            driveStraight(-reverseDist, robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)
            raiseLift(robot)
            driveStraight(-segment / 2, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment / 2, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            preTurn(robot)
            raiseTurn("R", robot)  # we turn two times instead of 180 degrees because I'm not sure the math will work.
            dropLift(robot)
            driveStraight(segment, robot)
            raiseLift(robot)
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - needs to be reviewed/tested - AC, 4/12

        if letter == "J":
            driveStraight(-reverseDist, robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)
            raiseLift(robot)
            driveStraight(-segment / 2, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment / 3, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment / 3, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done, needs to be reviewed/tested - AC, 4/12

        if letter == "K":
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            raiseLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurnR157(robot)
            dropLift(robot)
            driveStraight(math.sqrt((1 / 4 * segment ** 2) + (segment ** 2)), robot)
            raiseLift(robot)
            preTurn(robot)
            raiseTurnL135(robot)
            dropLift(robot)
            driveStraight(math.sqrt(1 / 4 * segment ** 2 + (segment ** 2)), robot)
            raiseLift(robot)
            preTurn(robot)
            raiseTurnL20(robot)
            driveStraight(space, robot)
            raiseTurn("L", robot)

        if letter == "L":
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            driveStraight(segment, robot)
            raiseLift(robot)
            driveStraight(-segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)
            raiseLift(robot)
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - needs to be reviewed/tested - AC, 4/12
        # I'll need more time to get M,N's math down.
        if letter == "M":
            pass
        if letter == "N":
            pass
        if letter == "O":
            # assuming this is a square O
            driveStraight(-reverseDist, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment, robot)
            raiseLift(robot)
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - needs to be reviewed/tested - AC, 4/12

        if letter == "P":
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            driveStraight(segment, robot)  # first segment
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # second segment: across the top
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)  # half-segment for the other side of P
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # bottom horizontal segment of P
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment / 2, robot)  # returns to initial position
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment + space, robot)  # this should get him to the next letter's initial position.
            preTurn(robot)
            raiseTurn("L", robot)
            #  Done - Still needs to be reviewed/tested - AC, 4/13
        if letter == "Q":
            pass
        if letter == "R":
            pass
        if letter == "S":
            driveStraight(-reverseDist, robot)  # init
            preTurn(robot)
            raiseTurn("R", robot)  # turn right to start.
            dropLift(robot)
            driveStraight(segment, robot)  # draw the bottom segment
            preTurn(robot)
            raiseTurn("L", robot)  # turn left
            dropLift(robot)
            driveStraight(segment / 2, robot)  # Draw the right vertical portion of the S
            preTurn(robot)
            raiseTurn("L", robot)  # Turn left
            dropLift(robot)
            driveStraight(segment, robot)  # Draw the middle horizontal segment
            preTurn(robot)
            raiseTurn("R", robot)  # turn right
            dropLift(robot)
            driveStraight(segment / 2, robot)  # draw the left vertical segment
            preTurn(robot)
            raiseTurn("R", robot)  # turn right
            dropLift(robot)
            driveStraight(segment, robot)  # draw the topmost vertical section
            preTurn(robot)
            raiseTurn("R", robot)  # turn right, destination is bottom right corner
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("L", robot)  # turn left to get into the next position
            driveStraight(space, robot)  # move forward " ".
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - Still needs to be reviewed/tested - AC, 4/13

        if letter == "T":
            driveStraight(-reverseDist, robot)
            preTurn(robot)
            raiseTurn("R", robot)  # turn right initially
            driveStraight(segment / 2, robot)
            preTurn(robot)
            raiseTurn("L", robot)  # turn left before starting to draw
            dropLift(robot)
            driveStraight(segment, robot)  # draw the vertical segment
            preTurn(robot)
            raiseTurn("R", robot)  # turn right, BUT reverse course 1/2 segment
            driveStraight(-segment / 2, robot)
            dropLift(robot)
            driveStraight(segment, robot)  # draw the horizontal component of T
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment, robot)  # heading down to bottom right corner
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - Needs to be reviewed/tested - AC, 4/13

        if letter == "U":
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            driveStraight(segment, robot)  # left vertical segment
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment, robot)  # move to next draw point at top right corner
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # right vertical segment
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(-segment, robot)  # reverse one full segment, we'll drop the lift and draw it next.
            dropLift(robot)
            driveStraight(segment, robot)  # low horizontal segment
            raiseLift(robot)
            driveStraight(space, robot)  # Move one space to start next letter
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - needs to be reviewed/tested - AC, 4/13
        if letter == "V":
            pass
        if letter == "W":
            pass
        if letter == "X":
            driveStraight(-reverseDist, robot)
            robot.turn_in_place(cozmo.util.degrees(-45), in_parallel=True).wait_for_completed()  # turn 45 degrees to
            # the right
            dropLift(robot)
            driveStraight(math.sqrt(2 * (segment ** 2)),
                          robot)  # The hypotenuse of a triangle with a = segment and b = segment is the square root of 2*segment^2.
            preTurn(robot)
            # we are at the top right corner now and need to turn left 135 degrees in order to drive straight to the
            # left corner.
            robot.turn_in_place(cozmo.util.degrees(135), in_parallel=True).wait_for_completed()
            # Not sure if below will work.
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            driveStraight(reverseDist, robot)
            driveStraight(math.sqrt(2 * (segment ** 2)),
                          robot)  # This will hopefully draw from top left to bottom right.

            preTurn(robot)
            robot.turn_in_place(cozmo.util.degrees(45), in_parallel=True).wait_for_completed()  # This will line us
            # back up, horizontally.
            # All we have to do is move forward one space, turn left and we're all set.
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - I'm very uneasy about how this will go, but I forgot my robot so I can't test it now.
            # - AC,  4/18

        if letter == "Y":
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment / 2, robot)  # drive us to the bottom of the middle segment
            preTurn(robot)
            raiseTurn("L", robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)  # draw the stem of Y
            preTurn(robot)
            raiseTurnL45(robot)  # draw the left diagonal of Y
            dropLift(robot)
            driveStraight(segment / 2, robot)  # the top prongs of Y should form an equilateral triangle with the top.
            # I don't think there's any special math required.
            preTurn(robot)
            raiseTurnR135(robot)
            driveStraight(segment / 2, robot)
            preTurn(robot)
            raiseTurnR135(robot)
            dropLift(robot)
            driveStraight(segment / 2, robot)  # this will draw from the top right portion back down to the stem
            preTurn(robot)
            raiseTurnL45(robot)
            driveStraight(segment / 2, robot)  # traverse to the bottom of the stem.
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight((segment / 2) + space,
                          robot)  # this will drive the rest of the segment AND the space to the next one.
            preTurn(robot)
            raiseTurn("L", robot)
            # DONE
            # I'm still not sure if this will work though.
            # AC - 4/18

        if letter == "Z":
            driveStraight(-reverseDist, robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment, robot)  # we have drawn top vertical segment.
            preTurn(robot)
            raiseTurnR135(robot)
            dropLift(robot)
            driveStraight(math.sqrt(2 * (segment ** 2)), robot)  # This should draw the diagonal segment of Z.
            preTurn(robot)
            raiseTurnL135(robot)
            dropLift(robot)
            driveStraight(segment, robot)
            raiseLift(robot)
            driveStraight(space, robot)
            preTurn(robot)
            raiseTurn("L", robot)
            # DONE - Needs testing. 4/22


print("ththth")
cozmo.run_program(cozmoAlphabet)