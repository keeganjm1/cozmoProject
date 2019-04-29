import cozmo
import socket
import errno
from socket import error as socket_error

# need to get movement info
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    global instructions
    """try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket_error as msg:
        robot.say_text("socket failed" + msg).wait_for_completed()
    ip = "10.0.1.10"
    port = 5000

    try:
        s.connect((ip, port))
    except socket_error as msg:
        robot.say_text("socket failed to bind").wait_for_completed()
    cont = True

    robot.say_text("ready").wait_for_completed()

    # SET COZMO's NAME
    
    myName2 = 2
    myName3 = 3
    myName4 = 4
    myName5 = 5
    myName6 = 6
    myName7 = 7
    myName8 = 8
    myName9 = 9

    while cont:
        bytedata = s.recv(4048)
        # data = str(bytedata)
        data = bytedata.decode('utf-8')
        if not data:
            cont = False
            s.close()
            quit()
        else:
            # ---------------------------------------------------------
            # This is where you need to adjust the program
            # ---------------------------------------------------------
"""
    myName1 = 1
    myName2 = 2
    myName3 = 3
    myName4 = 4
    myName5 = 5
    myName6 = 6
    myName7 = 7
    myName8 = 8
    myName9 = 9
    instructions = "A;9"
    instructions = instructions.split(';')
    #instructions = instructions[0:-1]
    myName = int(instructions[1])
    iowaDict = {'I': list(range(1,10))}
    print(instructions)
    while iowaDict is True:
        for key in iowaDict.iterkeys():
            for myName in iowaDict.itervalues():
                if key == "I":
                    if myName == 1:
                        robot.drive_straight(cozmo.util.distance_mm(406.4),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(304.8),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()


                # mac_cheese

                    if myName == 2:
                        robot.drive_straight(cozmo.util.distance_mm(304.8),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(304.8),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()

                # robot 3 qill drive striaght 101.6 mm turn right(-90), then drive straight for 203.2 mm and then turn vertical(left 90)
                    if myName == 3:
                        robot.drive_straight(cozmo.util.distance_mm(101.6),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(203.2),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                # robot 4 will turn horizontally

                    if myName == 4:
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()

                # robot 5 will turn horizontally
                    if  myName == 5:
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()


                # robot 6 will turn horizontally

                    if myName == 6:
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()


                    if myName == 7:
                        robot.drive_straight(cozmo.util.distance_mm(203.2),
                                             cozmo.util.speed_mmps(150)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(203.2),
                                             cozmo.util.speed_mmps(150)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()



                    if myName == 8:
                        robot.drive_straight(cozmo.util.distance_mm(406.4),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(304.8),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()


                    if myName == 9:
                        robot.drive_straight(cozmo.util.distance_mm(406.4),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(304.8),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                if key == 'O':
                    #print('got O')
                    if myName == 1:
                        robot.drive_straight(cozmo.util.distance_mm(292.1),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-80)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(342.9),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 2:
                        robot.drive_straight(cozmo.util.distance_mm(215.9),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(101.6),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(45)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(63.5),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 3:
                        robot.drive_straight(cozmo.util.distance_mm(152.4),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(30)).wait_for_completed()
                        #robot.drive_straight(cozmo.util.distance_mm(203.2),
                         #                    cozmo.util.speed_mmps(200)).wait_for_completed()
                        #robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    if myName == 4:
                        robot.drive_straight(cozmo.util.distance_mm(25.6),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(45)).wait_for_completed()
                    if myName == 5:
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    if myName == 6:
                        robot.drive_straight(cozmo.util.distance_mm(25.6),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-45)).wait_for_completed()

                    if myName == 7:
                        robot.drive_straight(cozmo.util.distance_mm(152.4),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-30)).wait_for_completed()


                    if myName == 8:
                        robot.drive_straight(cozmo.util.distance_mm(215.9),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(101.6),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-45)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(63.5),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 9:
                        robot.drive_straight(cozmo.util.distance_mm(292.1),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(80)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(342.9),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()


                if key == 'W':
                    if myName == 1:
                        robot.drive_straight(cozmo.util.distance_mm(279.4),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 2:
                        robot.drive_straight(cozmo.util.distance_mm(171.5),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 3:
                        robot.drive_straight(cozmo.util.distance_mm(89.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    if myName == 4:
                        robot.drive_straight(cozmo.util.distance_mm(165.1),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 5:
                        robot.drive_straight(cozmo.util.distance_mm(266.7),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    if myName == 6:
                        robot.drive_straight(cozmo.util.distance_mm(165.1),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 7:
                        robot.drive_straight(cozmo.util.distance_mm(89.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    if myName == 8:
                        robot.drive_straight(cozmo.util.distance_mm(171.5),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 9:
                        robot.drive_straight(cozmo.util.distance_mm(279.4),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                if key == 'A':
                    if myName == 1:
                        robot.drive_straight(cozmo.util.distance_mm(520.7),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(378.5),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 2:
                        robot.drive_straight(cozmo.util.distance_mm(150.1),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(90.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    if myName == 3:
                        robot.drive_straight(cozmo.util.distance_mm(254.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(38.1),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    if myName == 4:
                        robot.drive_straight(cozmo.util.distance_mm(400.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 5:
                        robot.drive_straight(cozmo.util.distance_mm(262.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(55.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 6:
                        robot.drive_straight(cozmo.util.distance_mm(400),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                    if myName == 7:
                        robot.drive_straight(cozmo.util.distance_mm(254.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(38.1),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    if myName == 8:
                        robot.drive_straight(cozmo.util.distance_mm(150.1),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(90.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()

                    if myName == 9:
                        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(335.9),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(260.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()
                        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                        robot.drive_straight(cozmo.util.distance_mm(20.0),
                                             cozmo.util.speed_mmps(200)).wait_for_completed()


""" 

            if len(instructions) > 5:
                if instructions[0] != myName:
                    for index,item in enumerate(instructions):
                        if item == myName:
                            if instructions[index+1]=="F" or instructions[index+1]=="B":
                                instructions = instructions[index:index+5]
                                break
                            else:
                                instructions = instructions[index:index+3]
                                break

            if instructions[0] == myName:   #check the name:
                if len(instructions) == 5:
                    #we know that this is a message involving movement
                    instructions[3] = int(instructions[3])
                    instructions[4] = int(instructions[4])
                    #next, we will want to move forward or backward, if the x distance is not 0
                    # first, just move if 'F' and turn 180 degrees for 'B'
                    if instructions[3] != 0:
                        if instructions[1] == "F":
                            robot.drive_straight(cozmo.util.distance_mm(instructions[3]), cozmo.util.speed_mmps(150)).wait_for_completed()
                        elif instructions[1] == "B":
                            robot.drive_straight(cozmo.util.distance_mm(-instructions[3]), cozmo.util.speed_mmps(150)).wait_for_completed()
                    #then, we will want to turn left or right, if the y distance is not 0
                    if instructions[4] != 0:
                        if instructions[2] == "L":
                            robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                            robot.drive_straight(cozmo.util.distance_mm(instructions[4]), cozmo.util.speed_mmps(150)).wait_for_completed()
                        elif instructions[2] == "R":
                            robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                            robot.drive_straight(cozmo.util.distance_mm(instructions[4]), cozmo.util.speed_mmps(150)).wait_for_completed()
                elif len(instructions) == 3:
                    head_angle = float(instructions[1])
                    head_angle = max(-25.0, min(head_angle, 44.5))
                    lift_arm = float(instructions[2])
                    lift_arm = max(0.0, min(lift_arm, 1.0))
                    robot.set_head_angle(degrees(head_angle)).wait_for_completed()
                    robot.set_lift_height(lift_arm, in_parallel=True).wait_for_completed()"""


cozmo.run_program(cozmo_program)
