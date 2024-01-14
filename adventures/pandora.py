import pyautogui
import numpy as np
from PIL import Image, ImageDraw
import time
import cv2
import logging
import re
import keyboard

logging.basicConfig(filename="../log/error_log.txt", level=logging.ERROR)

ANGLES_IMAGES_PATH = [
    {"key": "-5", "path": "../img/ant/ang/ang_-5.png"},
    {"key": "6", "path": "../img/ant/ang/ang_6.png"},
    {"key": "10", "path": "../img/ant/ang/ang_10.png"},
    {"key": "11", "path": "../img/ant/ang/ang_11.png"},
    {"key": "12", "path": "../img/ant/ang/ang_12.png"},
    {"key": "13", "path": "../img/ant/ang/ang_13.png"},
    {"key": "14", "path": "../img/ant/ang/ang_14.png"},
    {"key": "15", "path": "../img/ant/ang/ang_15.png"},
    {"key": "16", "path": "../img/ant/ang/ang_16.png"},
    {"key": "17", "path": "../img/ant/ang/ang_17.png"},
    {"key": "19", "path": "../img/ant/ang/ang_19.png"},
    {"key": "30", "path": "../img/ant/ang/ang_30.png"},
    {"key": "41", "path": "../img/ant/ang/ang_41.png"},
    {"key": "46", "path": "../img/ant/ang/ang_46.png"},
    {"key": "51", "path": "../img/ant/ang/ang_51.png"},
    {"key": "-5", "path": "../img/ant/ang/-5.png"},
    {"key": "6", "path": "../img/ant/ang/6.png"},
    {"key": "10", "path": "../img/ant/ang/10.png"},
    {"key": "10", "path": "../img/ant/ang/10_1.png"},
    {"key": "17", "path": "../img/ant/ang/17.png"},
    {"key": "41", "path": "../img/ant/ang/41.png"},
    {"key": "46", "path": "../img/ant/ang/46.png"},
    {"key": "10", "path": "../img/ant/ang/ang_10_1.png"},
]

ANGLE_ADJUSTED = False
W_PRESSED = False


def find_image(image_path, confidence=0.9):
    result = {"found": False, "position_x": 0, "position_y": 0}
    try:
        template = cv2.imread(image_path)
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
        with open("../log/log.txt", "a") as log_file:
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


def adjust_angle(max):
    global ANGLE_ADJUSTED
    if not ANGLE_ADJUSTED:
        print("adjusting angle...")
        i = 0
        while i < max:
            keyboard.press_and_release("w")
            i += 1
        ANGLE_ADJUSTED = True


def bar_on(duration):
    keyboard.press("space")
    time.sleep(float(duration))
    keyboard.release("space")


def round_boss():
    global W_PRESSED, ANGLE_ADJUSTED
    W_PRESSED = False
    
    for angle in ANGLES_IMAGES_PATH:
        key = angle["key"]
        result = find_image(angle["path"])

        if result["found"]:
            x = result["x"]
            y = result["y"]
            width = result["width"]
            height = result["height"]
            print(f"angle: '{key}' x: {x} y: {y} width: {width} height: {height}")

            attack_boss()

            if key == "41":
                bar_on(1.9)
            elif key == "46":
                bar_on(1.5)
            elif key == "51":
                bar_on(1.2)
            elif key == "-5":
                if not W_PRESSED:
                    adjust_angle(39)

                bar_on(2.1)
            elif key == "6":
                if not W_PRESSED:
                    adjust_angle(30)

                bar_on(2.1)
            elif key == "30":
                bar_on(2.1)
            else:
                if not W_PRESSED:
                    adjust_angle(23)

                bar_on(2.1)
            W_PRESSED = False

            break
        else:
          attack_boss()
          bar_on(2.1)

    time.sleep(1.5)