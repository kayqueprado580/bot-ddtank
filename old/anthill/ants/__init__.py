import pyautogui
import time
import cv2
import logging
import keyboard
import numpy as np
import ctypes
import sys
from PIL import Image

logging.basicConfig(filename="../log/error_log.txt", level=logging.ERROR)


IMAGES_ANTS_LEFT = [
    {"key": "ant_left", "path": "img/ants/ant_red_left.png"},
    {"key": "ant_left", "path": "img/ants/ant_blue_left.png"},
]
IMAGES_ANTS_RIGHT = [
    {"key": "ant_right", "path": "img/ants/red_ant_right.png"},
    {"key": "ant_right", "path": "img/ants/ant_blue_right.png"},
]

# SETTINGS TURN
FLY_USED = False
MONSTER_FOUND = False
SIDE = 0  # SIDE 0 = RIGHT | SIDE 1 = LEFT
MAX_SIDE_TURN = 5
COUNT_TURN_ANTS_LEFT = 0
COUNT_TURN_ANTS_RIGHT = 0


def set_default_parameters_ants():
    global SIDE, FLY_USED, MONSTER_FOUND, COUNT_TURN_ANTS_LEFT, COUNT_TURN_ANTS_RIGHT
    SIDE = 0
    FLY_USED = False
    MONSTER_FOUND = False
    COUNT_TURN_ANTS_LEFT = 0
    COUNT_TURN_ANTS_RIGHT = 0


def find_image(image_path, confidence=0.7):
    result = {"found": False, "position_x": 0, "position_y": 0}
    try:
        template = cv2.imread(image_path)
        position = pyautogui.locateOnScreen(template, confidence=confidence)

        if position is not None:
            x, y, _, _ = position
            result["found"] = True
            result["position_x"] = x
            result["position_y"] = y

    except Exception as e:
        error_message = f"An error occurred: {e}"
        logging.error(error_message)
        with open("../log/log.txt", "a") as log_file:
            log_file.write(error_message + "\n")

    return result


def fly():
    global FLY_USED
    if not FLY_USED:
        print("use fly...")
        result = find_image("img/fly.png")
        if result["found"]:
            x = result["position_x"]
            y = result["position_y"]
            pyautogui.click(result["position_x"], result["position_y"])
            keyboard.press_and_release("f")
            keyboard.press("space")
            time.sleep(0.8)
            keyboard.release("space")
            time.sleep(2)
        FLY_USED = True


def attack_ants():
    global FLY_USED

    time.sleep(0.4)
    keyboard.press_and_release("2")
    time.sleep(0.3)
    keyboard.press_and_release("4")
    time.sleep(0.2)
    keyboard.press_and_release("7")
    time.sleep(0.1)
    keyboard.press("space")
    if FLY_USED:
        time.sleep(0.3)
    else:
        time.sleep(0.5)
    keyboard.release("space")
    time.sleep(2)


def walking():
    global SIDE, FLY_USED

    if FLY_USED:
        if SIDE == 1:
            SIDE = 0
        else:
            SIDE = 1

    if SIDE == 1:
        print("left")
        keyboard.press("a")
        time.sleep(0.1)
        keyboard.release("a")
    else:
        print("right")
        keyboard.press("d")
        time.sleep(0.1)
        keyboard.release("d")


def look_ants_left():
    global FLY_USED, SIDE, COUNT_TURN_ANTS_LEFT, MONSTER_FOUND, IMAGES_ANTS_LEFT, MAX_SIDE_TURN
    for img_ants_left in IMAGES_ANTS_LEFT:
        key = img_ants_left["key"]
        ants_left = find_image(img_ants_left["path"])
        if ants_left["found"]:
            print("monsters on the left")
            SIDE = 1
            COUNT_TURN_ANTS_LEFT += 1
            MONSTER_FOUND = True
            if COUNT_TURN_ANTS_LEFT > MAX_SIDE_TURN and not FLY_USED:
                SIDE = 0
                COUNT_TURN_ANTS_LEFT = 0
            break
    return MONSTER_FOUND


def look_ants_right():
    global FLY_USED, SIDE, COUNT_TURN_ANTS_RIGHT, MONSTER_FOUND, IMAGES_ANTS_RIGHT, MAX_SIDE_TURN
    for img_ants_right in IMAGES_ANTS_RIGHT:
        key = img_ants_right["key"]
        antes_righ = find_image(img_ants_right["path"])
        if antes_righ["found"]:
            print("monsters on the right")
            SIDE = 0
            COUNT_TURN_ANTS_RIGHT += 1
            MONSTER_FOUND = True

            if COUNT_TURN_ANTS_RIGHT > MAX_SIDE_TURN and not FLY_USED:
                SIDE = 1
                COUNT_TURN_ANTS_RIGHT = 0
            break
    return MONSTER_FOUND


def turn_on_stage_ants():
    global MONSTER_FOUND
    while True:
        look_ants_left()
        if not MONSTER_FOUND:
            look_ants_right()

        if MONSTER_FOUND:
            walking()
            attack_ants()
            time.sleep(3)
            MONSTER_FOUND = False
            break
        time.sleep(0.3)
