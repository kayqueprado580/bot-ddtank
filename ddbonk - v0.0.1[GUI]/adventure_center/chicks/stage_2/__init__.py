import pyautogui
import time
import cv2
import logging
import keyboard
import sys

from lib import turnon

# SETTINGS TURN
COUNT_TURN = 0
ADJUSTED_ANGLE = False
COUNT_GET_TRY_ANGLE = 0
KEY = 0

logging.basicConfig(filename="../log/error_log.txt", level=logging.ERROR)


def find_image(image_path, confidence=0.9):
    result = {"found": False, "position_x": 0, "position_y": 0}
    try:
        template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        position = pyautogui.locateOnScreen(template, confidence=confidence)

        if position is not None:
            x, y, width, height = position
            result["found"] = True
            result["x"] = x
            result["y"] = y
            result["width"] = width
            result["height"] = height

    except Exception as e:
        error_message = f"An error occurred: {e}"
        logging.error(error_message)
        with open("..log/log.txt", "a") as log_file:
            log_file.write(error_message + "\n")

    return result


def set_default_parameters_stage_2():
    global GET_SIDE, SIDE, FLY_USED, COUNT_TURN, MAX_TURN, MAX_TURN_BASE
    GET_SIDE = False
    FLY_USED = False
    SIDE = 0
    COUNT_TURN = 0
    MAX_TURN = MAX_TURN_BASE


def attack():
    keyboard.press_and_release("3")
    keyboard.press_and_release("4")
    keyboard.press_and_release("4")
    keyboard.press_and_release("5")
    keyboard.press_and_release("5")
    keyboard.press_and_release("6")
    keyboard.press_and_release("6")
    keyboard.press_and_release("7")
    keyboard.press_and_release("7")
    keyboard.press_and_release("8")
    keyboard.press_and_release("8")


def adjust_angle(max):
    global ADJUSTED_ANGLE
    time.sleep(0.2)

    if not ADJUSTED_ANGLE:
        print("adjusting angle...")
        i = 0
        while i < max:
            keyboard.press_and_release("w")
            time.sleep(0.07)
            i += 1
        ADJUSTED_ANGLE = True


def check_angles(key):
    force = 3
    if key == "-5":
        adjust_angle(33)
        force = 2.1
    elif key == "0":
        adjust_angle(29)
        force = 2.1
    elif key == "6" or key == "7":
        adjust_angle(24)
        force = 2.1
    elif key == "10" or key == "11" or key == "12":
        adjust_angle(20)
        force = 2.1
    elif key == "13" or key == "14" or key == "15":
        adjust_angle(18)
        force = 2.1
    elif key == "16" or key == "17" or key == "19":
        adjust_angle(16)
        force = 2.1
    elif key == "30":
        force = 2.1
    elif key == "41":
        force = 1.9
    elif key == "46":
        force = 1.5
    elif key == "51":
        force = 1.2
    elif key == "47":
        force = 1.6
    else:
        force = 2.1

    return force


def bar_on(duration):
    keyboard.press("space")
    time.sleep(float(duration))
    keyboard.release("space")


def set_adjusted_angle(flag):
    global ADJUSTED_ANGLE
    ADJUSTED_ANGLE = flag


def set_count_try_angle():
    global COUNT_GET_TRY_ANGLE
    COUNT_GET_TRY_ANGLE = 0


def turn_on_stage_2():
    global COUNT_GET_TRY_ANGLE, ADJUSTED_ANGLE, KEY
    time.sleep(1)

    print(f"ADJUSTED_ANGLE: {ADJUSTED_ANGLE}")
    num_positions = len(ANGLES_IMAGES_PATH) * 2
    count = 0

    if not ADJUSTED_ANGLE:
        for angle in turnon.IMAGES_ANGLES:
            key = angle["key"]
            KEY = key
            result = find_image(angle["path"])

            if result["found"]:
                print(f"angle: '{key}'")
                time.sleep(0.2)
                attack_boss()
                time.sleep(0.3)
                force = check_angles(key)
                time.sleep(0.3)
                bar_on(force)
                time.sleep(2.5)
                break
            else:
                print(
                    f"attempt counter to get the angle: {COUNT_GET_TRY_ANGLE} of max try: {num_positions}"
                )
                if COUNT_GET_TRY_ANGLE >= int(num_positions):
                    print(f"not found angle")
                    attack_boss()
                    bar_on(2.5)
                    time.sleep(5)
                    COUNT_GET_TRY_ANGLE = 0
                    break
                else:
                    COUNT_GET_TRY_ANGLE += 1
    else:
        time.sleep(0.2)
        attack_boss()
        time.sleep(0.3)
        force = check_angles(KEY)
        time.sleep(0.3)
        bar_on(force)
        time.sleep(2.5)

    time.sleep(1)
