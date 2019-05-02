import cozmo
import time
import socket
import select




# face display stuff
"""
Copyright Kinvert All Rights Reserved
If you would like to use this code for
business or education please contact
us for permission at:
www.kinvert.com/
"""
import cozmo
import time

try:
    from PIL import Image
except:
    print("Looks like you need to install Pillow")


    robot.say_text("ready robot eight").wait_for_completed()
    # SET COZMO's NAME

    '''myName2 = 2
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
'''
def cozmo_program(robot: cozmo.robot.Robot):

    robot.set_lift_height(0).wait_for_completed()
    robot.set_head_angle(cozmo.util.degrees(0)).wait_for_completed()

    robot.say_text("go hawks!").wait_for_completed()

    image = Image.open("IOWAlogo.jpg")
    image = image.resize(cozmo.oled_face.dimensions(), Image.NEAREST)
    image = cozmo.oled_face.convert_image_to_screen_data(image)

    seconds = 5

    robot.set_head_angle(cozmo.util.degrees(44.5)).wait_for_completed()

    for nothing in range(seconds):
        robot.display_oled_face_image(image, 1000.0)
        time.sleep(1.0)

    time.sleep(1.0)

    robot.set_head_angle(cozmo.util.degrees(0)).wait_for_completed()



    instructions = "O"
    for item in instructions:
        if item == "I":
            image = Image.open("I.png")
            image = image.resize(cozmo.oled_face.dimensions(), Image.NEAREST)
            image = cozmo.oled_face.convert_image_to_screen_data(image)

            seconds = 10

            # forward

            robot.say_text("I", duration_scalar=1.5, voice_pitch=0.5).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(656.4),
                                 cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
            time.sleep(2)
            robot.drive_straight(cozmo.util.distance_mm(384.8),
                                 cozmo.util.speed_mmps(200)).wait_for_completed()
            # sleep
            #time.sleep(10)

            robot.set_head_angle(cozmo.util.degrees(44.5)).wait_for_completed()

            for nothing in range(seconds):
                robot.display_oled_face_image(image, 1000.0)
                time.sleep(1.0)
            time.sleep(0.5)

            robot.set_head_angle(cozmo.util.degrees(0)).wait_for_completed()

            # reverse
            robot.drive_straight(cozmo.util.distance_mm(-384.8),
                                 cozmo.util.speed_mmps(200)).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(-656.4),
                                 cozmo.util.speed_mmps(200)).wait_for_completed()

        if item == "O":
            image = Image.open("o.png")
            image = image.resize(cozmo.oled_face.dimensions(), Image.NEAREST)
            image = cozmo.oled_face.convert_image_to_screen_data(image)

            seconds = 4

            robot.say_text("O", duration_scalar=1.5, voice_pitch=0.5).wait_for_completed()
            # forward

            if item == "O":
                # forward
                robot.drive_straight(cozmo.util.distance_mm(345),
                                     cozmo.util.speed_mmps(250)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(80)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(370),
                                     cozmo.util.speed_mmps(250)).wait_for_completed()

                # sleep
                #time.sleep(4)
                robot.set_head_angle(cozmo.util.degrees(44.5)).wait_for_completed()

                for nothing in range(seconds):
                    robot.display_oled_face_image(image, 1000.0)
                    time.sleep(1.0)
                time.sleep(0.5)

                robot.set_head_angle(cozmo.util.degrees(0)).wait_for_completed()

                # reverse
                robot.drive_straight(cozmo.util.distance_mm(-370),
                                     cozmo.util.speed_mmps(250)).wait_for_completed()
                robot.turn_in_place(cozmo.util.degrees(-80)).wait_for_completed()
                robot.drive_straight(cozmo.util.distance_mm(-345),
                                     cozmo.util.speed_mmps(250)).wait_for_completed()

                if item == "W":
                    # forward
                    robot.drive_straight(cozmo.util.distance_mm(279.4),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()

                    # sleep
                    time.sleep(10)

                    # reverse
                    robot.drive_straight(cozmo.util.distance_mm(-279.4),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()

                if item == "A":
                    # forward
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(335.9),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(260.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(20.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()

                    # sleep
                    time.sleep(10)

                    # reverse
                    robot.drive_straight(cozmo.util.distance_mm(-20.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(-260.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(-335.9),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()


cozmo.run_program(cozmo_program)