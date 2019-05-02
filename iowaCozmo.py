import cozmo
import socket
import errno
from socket import error as socket_error

# need to get movement info
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):

    instructions = "O;8"
    instructions = instructions.split(';')
    #instructions = instructions[0:-1]
    myName = int(instructions[1])
    iowaDict = {'O': list(range(0,9))}
    print(instructions)
    i=0

    #for key in iowaDict.keys():
    for key in instructions:
        if key== "I":
            if instructions[1] == 0:
                robot.drive_straight(cozmo.util.distance_mm(406.4),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(304.8),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()


        # mac_cheese

            if instructions[1] == 1:
                robot.drive_straight(cozmo.util.distance_mm(304.8),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(304.8),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()

        # robot 3 qill drive striaght 101.6 mm turn right(-90), then drive straight for 203.2 mm and then turn vertical(left 90)
            if instructions[1] == 2:
                robot.drive_straight(cozmo.util.distance_mm(101.6),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(203.2),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
        # robot 4 will turn horizontally

            if instructions[1] == 3:
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()

        # robot 5 will turn horizontally
            if instructions[1] == 4:
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()


        # robot 6 will turn horizontally

            if instructions[1] == 5:
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()


            if instructions[1] == 6:
                robot.drive_straight(cozmo.util.distance_mm(203.2),
                                     cozmo.util.speed_mmps(150)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(203.2),
                                     cozmo.util.speed_mmps(150)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()



            if instructions[1] == 7:
                robot.drive_straight(cozmo.util.distance_mm(406.4),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(304.8),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()


            if instructions[1] == 8:
                robot.drive_straight(cozmo.util.distance_mm(406.4),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(304.8),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
        if key == 'O':
            print('got O')
            if instructions[1] == '0':
                print("ye")
                robot.drive_straight(cozmo.util.distance_mm(292.1),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-80)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(342.9),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i+1
            if instructions[1] == '1':
                robot.drive_straight(cozmo.util.distance_mm(215.9),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(101.6),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(45)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(63.5),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == '2':
                robot.drive_straight(cozmo.util.distance_mm(135),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(30)).wait_for_completed()
                #robot.drive_straight(cozmo.util.distance_mm(203.2),
                 #                    cozmo.util.speed_mmps(200)).wait_for_completed()
                #robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                i = i + 1
            if instructions[1] == '3':
                robot.drive_straight(cozmo.util.distance_mm(25.6),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(45)).wait_for_completed()
                i = i + 1
            if instructions[1] == '4':
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                i = i + 1
            if instructions[1] == '5':
                robot.drive_straight(cozmo.util.distance_mm(25.6),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-45)).wait_for_completed()
                i = i + 1

            if instructions[1] == '6':
                robot.drive_straight(cozmo.util.distance_mm(152.4),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-30)).wait_for_completed()
                i = i + 1


            if instructions[1] == '7':
                robot.drive_straight(cozmo.util.distance_mm(288.9),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(103.6),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-45)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(63.5),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == '8':
                robot.drive_straight(cozmo.util.distance_mm(345),
                                     cozmo.util.speed_mmps(250)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(80)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(370),
                                     cozmo.util.speed_mmps(250)).wait_for_completed()
                i = i + 1


        if key == 'W':
            if instructions[1] == 0:
                robot.drive_straight(cozmo.util.distance_mm(279.4),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == 1:
                robot.drive_straight(cozmo.util.distance_mm(171.5),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == 2:
                robot.drive_straight(cozmo.util.distance_mm(89.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                i = i + 1
            if instructions[1] == 3:
                robot.drive_straight(cozmo.util.distance_mm(165.1),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == 4:
                robot.drive_straight(cozmo.util.distance_mm(266.7),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                i = i + 1
            if instructions[1] == 5:
                robot.drive_straight(cozmo.util.distance_mm(165.1),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == 6:
                robot.drive_straight(cozmo.util.distance_mm(89.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                i = i + 1
            if instructions[1] == 7:
                robot.drive_straight(cozmo.util.distance_mm(171.5),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == 8:
                robot.drive_straight(cozmo.util.distance_mm(279.4),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
        if key == 'A':
            if instructions[1] == 0:
                robot.drive_straight(cozmo.util.distance_mm(520.7),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(378.5),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == 1:
                robot.drive_straight(cozmo.util.distance_mm(150.1),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(90.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                i = i + 1
            if instructions[1] == 2:
                robot.drive_straight(cozmo.util.distance_mm(254.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(38.1),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                i = i + 1
            if instructions[1] == 3:
                robot.drive_straight(cozmo.util.distance_mm(400.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == 4:
                robot.drive_straight(cozmo.util.distance_mm(262.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(55.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == 5:
                robot.drive_straight(cozmo.util.distance_mm(400),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1
            if instructions[1] == 6:
                robot.drive_straight(cozmo.util.distance_mm(254.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(38.1),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                i = i + 1
            if instructions[1] == 7:
                robot.drive_straight(cozmo.util.distance_mm(150.1),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(90.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                i = i + 1

            if instructions[1] == 8:
                robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(335.9),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(260.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(20.0),
                                     cozmo.util.speed_mmps(200)).wait_for_completed()
                i = i + 1


        """ 
        
        if instructions[1]nstructions) > 5:
        if instructions[1]uctions[0] != myName:
            for index,item in enumerate(instructions):
                if instructions[1]== myName:
                    if instructions[1]uctions[index+1]=="F" or instructions[index+1]=="B":
                        instructions = instructions[index:index+5]
                        break
                    else:
                        instructions = instructions[index:index+3]
                        break
        
        if instructions[1]uctions[0] == myName:   #check the name:
        if instructions[1]nstructions) == 5:
            #we know that this is a message involving movement
            instructions[3] = int(instructions[3])
            instructions[4] = int(instructions[4])
            #next, we will want to move forward or backward, if instructions[1] distance is not 0
            # first, just move if instructions[1]nd turn 180 degrees for 'B'
            if instructions[1]uctions[3] != 0:
                if instructions[1]uctions[1] == "F":
                    robot.drive_straight(cozmo.util.distance_mm(instructions[3]), cozmo.util.speed_mmps(150)).wait_for_completed()
                elif instructions[1]uctions[1] == "B":
                    robot.drive_straight(cozmo.util.distance_mm(-instructions[3]), cozmo.util.speed_mmps(150)).wait_for_completed()
            #then, we will want to turn left or right, if instructions[1] distance is not 0
            if instructions[1]uctions[4] != 0:
                if instructions[1]uctions[2] == "L":
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(instructions[4]), cozmo.util.speed_mmps(150)).wait_for_completed()
                elif instructions[1]uctions[2] == "R":
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(instructions[4]), cozmo.util.speed_mmps(150)).wait_for_completed()
        elif instructions[1]nstructions) == 3:
            head_angle = float(instructions[1])
            head_angle = max(-25.0, min(head_angle, 44.5))
            liftinstructions[1]= float(instructions[2])
            liftinstructions[1]= max(0.0, min(liftinstructions[1] 1.0))
            robot.set_head_angle(degrees(head_angle)).wait_for_completed()
            robot.set_liftinstructions[1]ht(liftinstructions[1] in_parallel=True).wait_for_completed()"""


cozmo.run_program(cozmo_program)
