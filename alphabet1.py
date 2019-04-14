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
    robot.set_lift_height(1, 15).wait_for_completed()  # lift comes up
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

        """   A, B, C, D, E all need to be fixed yet."""
        if letter == 'F':
            # Setup and drop Lift
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            # Drive forward one full segment (Left vertical component of F
            driveStraight(segment, robot)
            # Preturn adjustments (call preTurn function)
            preTurn(robot)
            #turn right to tackle the high-horizontal component of F
            raiseTurn("R", robot)
            dropLift(robot)  # ready to draw
            driveStraight(segment)  # top horizontal line completed
            # preTurn, turn right, and drive down 1/2 of a segment to get to middle-height of the right side of F
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment/2)
            #now we turn right, move forward another half of a segment before we can start drawing the middle horizontal line of F
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment/2)
            # now we'r ready to draw that line (1/2 segment long)
            dropLift(robot)
            driveStraight(segment/2)
            # turn left and drive down to where we started, before driving over to the next ready position
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment + space)
            #turn left to get to next ready position and we're done.
            preTurn(robot)
            raiseTurn("L", robot)
            # F is done and ready to be reviewed. - AC
        #Remind me to ask you about string input vs. list input.
        if letter == "G":
            driveStraight(-reverseDist, robot)
            dropLift(robot)
            driveStraight(segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight((3/4) * segment)
            dropLift(robot)
            driveStraight((1/4)*segment)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight((1/4)*segment, robot)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment/2)
            dropLift(robot)
            driveStraight(segment/2)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment/4)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(space)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done, will need to be reviewed/tested -AC, 4/11

        if letter == "H":
            driveStraight(-reverseDist)
            dropLift(robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment/2)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)
            raiseLift(robot)
            driveStraight(-segment)
            preTurn(robot)
            raiseTurn("L", robot)
            dropLift(robot)
            driveStraight(segment/2)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(space)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done, needs to be reviewed/tested - AC, 4/11


        if letter == "I":
            driveStraight(-reverseDist)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)
            raiseLift(robot)
            driveStraight(-segment/2)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment/2)
            preTurn(robot)
            raiseTurn("R", robot)
            preTurn(robot)
            raiseTurn("R", robot)  # we turn two times instead of 180 degrees because I'm not sure the math will work.
            dropLift(robot)
            driveStraight(segment)
            raiseLift(robot)
            driveStraight(space)
            preTurn(robot)
            raiseTurn("L", robot)
            #Done - needs to be reviewed/tested - AC, 4/12

        if letter == "J":
            driveStraight(-reverseDist)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)
            raiseLift(robot)
            driveStraight(-segment/2)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment/2)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment/3)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment/3)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(space)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done, needs to be reviewed/tested - AC, 4/12

        if letter == "K":
            pass
        if letter == "L":
            driveStraight(-reverseDist)
            dropLift(robot)
            driveStraight(segment)
            raiseLift(robot)
            driveStraight(-segment)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)
            raiseLift(robot)
            driveStraight(space)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - needs to be reviewed/tested - AC, 4/12
        # I'll need more time to get M,N's math down.
        if letter == "M":
            pass
        if letter == "N":
            pass
        if letter == "O":
            #assuming this is a square O
            driveStraight(-reverseDist)
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment)
            raiseLift(robot)
            driveStraight(space)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - needs to be reviewed/tested - AC, 4/12

        if letter == "P":
            driveStraight(-reverseDist)
            dropLift(robot)
            driveStraight(segment)  # first segment
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)  # second segment: across the top
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment/2)  # half-segment for the other side of P
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)  # bottom horizontal segment of P
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment/2)  # returns to initial position
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(segment + space)  # this should get him to the next letter's initial position.
            preTurn(robot)
            raiseTurn("L", robot)
            #  Done - Still needs to be reviewed/tested - AC, 4/13
        if letter == "Q":
            pass
        if letter == "R":
            pass
        if letter == "S":
            driveStraight(-reverseDist)  # init
            preTurn(robot)
            raiseTurn("R", robot)  # turn right to start.
            dropLift(robot)
            driveStraight(segment)  # draw the bottom segment
            preTurn(robot)
            raiseTurn("L", robot)  # turn left
            dropLift(robot)
            driveStraight(segment/2)  # Draw the right vertical portion of the S
            preTurn(robot)
            raiseTurn("L", robot)  # Turn left
            dropLift(robot)
            driveStraight(segment)  # Draw the middle horizontal segment
            preTurn(robot)
            raiseTurn("R", robot)  # turn right
            dropLift(robot)
            driveStraight(segment/2)  # draw the left vertical segment
            preTurn(robot)
            raiseTurn("R", robot)  # turn right
            dropLift(robot)
            driveStraight(segment)  # draw the topmost vertical section
            preTurn(robot)
            raiseTurn("R", robot)  # turn right, destination is bottom right corner
            driveStraight(segment)
            preTurn(robot)
            raiseTurn("L", robot)  # turn left to get into the next position
            driveStraight(space)  # move forward " ".
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - Still needs to be reviewed/tested - AC, 4/13

        if letter == "T":
            driveStraight(-reverseDist)
            preTurn(robot)
            raiseTurn("R", robot)  # turn right initially
            driveStraight(segment/2)
            preTurn(robot)
            raiseTurn("L", robot)  # turn left before starting to draw
            dropLift(robot)
            driveStraight(segment)  # draw the vertical segment
            preTurn(robot)
            raiseTurn("R", robot)  # turn right, BUT reverse course 1/2 segment
            driveStraight(-segment/2)
            dropLift(robot)
            driveStraight(segment)  # draw the horizontal component of T
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment)  # heading down to bottom right corner
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(space)
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - Needs to be reviewed/tested - AC, 4/13


        if letter == "U":
            driveStraight(-reverseDist)
            dropLift(robot)
            driveStraight(segment)  # left vertical segment
            preTurn(robot)
            raiseTurn("R", robot)
            driveStraight(segment)  # move to next draw point at top right corner
            preTurn(robot)
            raiseTurn("R", robot)
            dropLift(robot)
            driveStraight(segment)  # right vertical segment
            preTurn(robot)
            raiseTurn("L", robot)
            driveStraight(-segment)  # reverse one full segment, we'll drop the lift and draw it next.
            dropLift(robot)
            driveStraight(segment)  # low horizontal segment
            raiseLift(robot)
            driveStraight(space)  # Move one space to start next letter
            preTurn(robot)
            raiseTurn("L", robot)
            # Done - needs to be reviewed/tested - AC, 4/13
        if letter == "V":
            pass
        if letter == "W":
            pass
        if letter == "X":
            pass
        if letter == "Y":
            pass
        if letter == "Z":
            pass







print("ththth")
cozmo.run_program(cozmoAlphabet)