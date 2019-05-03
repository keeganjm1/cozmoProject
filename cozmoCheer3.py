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

    robot.say_text("ready robot zero").wait_for_completed()

    while 1:
        bytedata = s.recv(4048)
        data = str(bytedata)
        instructions = bytedata.decode('utf-8')
        if not data:
            cont = False
            s.close()
            quit()
        else:

            time.sleep(4.5)

            robot.set_lift_height(1.0).wait_for_completed()
            robot.turn_in_place(cozmo.util.degrees(-360)).wait_for_completed()
            robot.set_lift_height(0).wait_for_completed()


cozmo.run_program(cozmo_program)
