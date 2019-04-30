import cozmo
import time
import socket
import select



def cozmo_program(robot: cozmo.robot.Robot):
    global instructions
    try:
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
        data = str(bytedata)
        instructions = bytedata.decode('utf-8')
        if not data:
            cont = False
            s.close()
            quit()
        else:
            # ---------------------------------------------------------
            # This is where you need to adjust the program
            # ---------------------------------------------------------

            # inst: 8
            for item in instructions:
                if item == "I":
                    # forward
                    robot.drive_straight(cozmo.util.distance_mm(406.4),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(304.8),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    # sleep
                    time.sleep(10)

                    # reverse
                    robot.drive_straight(cozmo.util.distance_mm(-304.8),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(-406.4),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()

                if item == "O":
                    # forward
                    robot.drive_straight(cozmo.util.distance_mm(215.9),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(101.6),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(-45)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(63.5),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    # sleep
                    time.sleep(10)

                    # reverse
                    robot.drive_straight(cozmo.util.distance_mm(-63.5),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(45)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(-101.6),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(
                        -91)).wait_for_completed()  # Gets closer to start with Alex's robot, might vary for others.
                    # robot.turn_in_place(cozmo.util.degrees(-92.5)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(-215.9),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()

                if item == "W":
                    # forward
                    robot.drive_straight(cozmo.util.distance_mm(171.5),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    # sleep
                    time.sleep(10)

                    # reverse
                    robot.drive_straight(cozmo.util.distance_mm(-171.5),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()

                if item == "A":
                    # forward
                    robot.drive_straight(cozmo.util.distance_mm(150.1),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(90.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()

                    # sleep
                    time.sleep(10)

                    # reverse
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(-90.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(-150.1),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()



cozmo.run_program(cozmo_program)