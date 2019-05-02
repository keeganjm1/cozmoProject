import cozmo
import time
import socket
import select

try:
    from PIL import Image
except:
    print("Looks like you need to install Pillow")


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

    robot.say_text("ready robot four").wait_for_completed()

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
            for item in instructions:
                if item == "I":

                    image = Image.open("I.png")
                    image = image.resize(cozmo.oled_face.dimensions(), Image.NEAREST)
                    image = cozmo.oled_face.convert_image_to_screen_data(image)

                    seconds = 10

                    robot.say_text("I", duration_scalar=1.5, voice_pitch=0.5).wait_for_completed()

                    # forward
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()

                    # sleep
                    #time.sleep(10)

                    robot.set_head_angle(cozmo.util.degrees(44.5)).wait_for_completed()

                    for nothing in range(seconds):
                        robot.display_oled_face_image(image, 1000.0)
                        time.sleep(1.0)
                    time.sleep(1.0)

                    robot.set_head_angle(cozmo.util.degrees(0)).wait_for_completed()

                    # reverse
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()

                if item == "O":

                    image = Image.open("o.png")
                    image = image.resize(cozmo.oled_face.dimensions(), Image.NEAREST)
                    image = cozmo.oled_face.convert_image_to_screen_data(image)

                    seconds = 18

                    robot.say_text("O", duration_scalar=1.5, voice_pitch=0.5).wait_for_completed()

                    # forward
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    # sleep
                    #time.sleep(18)

                    robot.set_head_angle(cozmo.util.degrees(44.5)).wait_for_completed()

                    for nothing in range(seconds):
                        robot.display_oled_face_image(image, 1000.0)
                        time.sleep(1.0)
                    time.sleep(1.0)

                    robot.set_head_angle(cozmo.util.degrees(0)).wait_for_completed()

                    # reverse
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()

                if item == "W":

                    image = Image.open("w.png")
                    image = image.resize(cozmo.oled_face.dimensions(), Image.NEAREST)
                    image = cozmo.oled_face.convert_image_to_screen_data(image)

                    seconds = 10

                    robot.say_text("W", duration_scalar=1.5, voice_pitch=0.5).wait_for_completed()

                    # forward
                    robot.drive_straight(cozmo.util.distance_mm(266.7),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    # sleep
                    #time.sleep(10)

                    robot.set_head_angle(cozmo.util.degrees(44.5)).wait_for_completed()

                    for nothing in range(seconds):
                        robot.display_oled_face_image(image, 1000.0)
                        time.sleep(1.0)
                    time.sleep(1.0)

                    robot.set_head_angle(cozmo.util.degrees(0)).wait_for_completed()

                    # reverse
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(-266.7),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()

                if item == "A":

                    image = Image.open("a.png")
                    image = image.resize(cozmo.oled_face.dimensions(), Image.NEAREST)
                    image = cozmo.oled_face.convert_image_to_screen_data(image)

                    seconds = 8

                    robot.say_text("A", duration_scalar=1.5, voice_pitch=0.5).wait_for_completed()

                    # forward
                    robot.drive_straight(cozmo.util.distance_mm(262.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(55.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    # sleep
                    #time.sleep(8)
                    # reverse

                    robot.set_head_angle(cozmo.util.degrees(44.5)).wait_for_completed()

                    for nothing in range(seconds):
                        robot.display_oled_face_image(image, 1000.0)
                        time.sleep(1.0)
                    time.sleep(1.0)

                    robot.set_head_angle(cozmo.util.degrees(0)).wait_for_completed()

                    robot.drive_straight(cozmo.util.distance_mm(-55.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()
                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                    robot.drive_straight(cozmo.util.distance_mm(-262.0),
                                         cozmo.util.speed_mmps(200)).wait_for_completed()


cozmo.run_program(cozmo_program)
