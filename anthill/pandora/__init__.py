import pyautogui
import numpy as np
from PIL import Image, ImageDraw
import time
import cv2
import logging
import re
import keyboard

logging.basicConfig(filename="log/error_log.txt", level=logging.ERROR)

ANGLES_IMAGES_PATH = [
    {"key": "-5", "path": "img/ang/ang_-5.png"},
    {"key": "6", "path": "img/ang/ang_6.png"},
    {"key": "10", "path": "img/ang/ang_10.png"},
    {"key": "11", "path": "img/ang/ang_11.png"},
    {"key": "12", "path": "img/ang/ang_12.png"},
    {"key": "13", "path": "img/ang/ang_13.png"},
    {"key": "14", "path": "img/ang/ang_14.png"},
    {"key": "15", "path": "img/ang/ang_15.png"},
    {"key": "16", "path": "img/ang/ang_16.png"},
    {"key": "17", "path": "img/ang/ang_17.png"},
    {"key": "19", "path": "img/ang/ang_19.png"},
    {"key": "30", "path": "img/ang/ang_30.png"},
    {"key": "41", "path": "img/ang/ang_41.png"},
    {"key": "46", "path": "img/ang/ang_46.png"},
    {"key": "51", "path": "img/ang/ang_51.png"},
    {"key": "-5", "path": "img/ang/-5.png"},
    {"key": "6", "path": "img/ang/6.png"},
    {"key": "6", "path": "img/ang/ang_6_1.png"},
    {"key": "10", "path": "img/ang/10.png"},
    {"key": "10", "path": "img/ang/10_1.png"},
    {"key": "17", "path": "img/ang/17.png"},
    {"key": "41", "path": "img/ang/41.png"},
    {"key": "46", "path": "img/ang/46.png"},
    {"key": "10", "path": "img/ang/ang_10_1.png"},
    {"key": "10", "path": "img/ang/ang_10_2.png"},
    {"key": "10", "path": "img/ang/ang_10_2.png"},
    {"key": "7", "path": "img/ang/ang_7.png"},
    {"key": "0", "path": "img/ang/ang_0.png"},
]


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
        with open("log/log.txt", "a") as log_file:
            log_file.write(error_message + "\n")

    return result


def attack_boss():
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


def set_adjusted_angle(flag):
    global ADJUSTED_ANGLE
    ADJUSTED_ANGLE = flag


ADJUSTED_ANGLE = False


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


COUNT_GET_TRY_ANGLE = 0


def set_count_try_angle():
    global COUNT_GET_TRY_ANGLE
    COUNT_GET_TRY_ANGLE = 0


def turn_on_boss():
    global COUNT_GET_TRY_ANGLE, ADJUSTED_ANGLE
    time.sleep(1)

    print(f"ADJUSTED_ANGLE: {ADJUSTED_ANGLE}")
    num_positions = len(ANGLES_IMAGES_PATH) * 2
    count = 0
    for angle in ANGLES_IMAGES_PATH:
        key = angle["key"]
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

    time.sleep(1)
