import pyautogui
import time
import cv2
import logging
import keyboard
import numpy as np
import ctypes
from PIL import Image

from cards import flip_cards
from pandora_sec import optional_round_boss
from pandora import round_boss


logging.basicConfig(filename="../log/error_log.txt", level=logging.ERROR)

IMAGES_PATH = [
    {"key": "start", "path": "../img/ant/start.png"},
    {"key": "my_turn", "path": "../img/pass.png"},
    {"key": "my_turn", "path": "../img/pass2.png"},
    {"key": "central", "path": "../img/central.png"},
    {"key": "play", "path": "../img/play_central.png"},
    {"key": "select", "path": "../img/select.png"},
    {"key": "card", "path": "../img/cards.png"},
    {"key": "selected_ant", "path": "../img/ant/selected_ant.png"},
    # {"key": "easy", "path": "../img/ant/easy.png"},
    {"key": "normal", "path": "../img/ant/normal.png"},
    {"key": "ok", "path": "../img/ant/ok.png"},
    {"key": "win", "path": "../img/ant/win.png"},
    {"key": "pandora_room", "path": "../img/ant/pandora_room.png"},
]

MONSTERS_IMAGES_PATH = [
    {"key": "pandora", "path": "../img/ant/pandora.png"},
    {"key": "pandora", "path": "../img/ant/pandora1.png"},
    {"key": "pandora", "path": "../img/ant/pandora2.png"},
    {"key": "pandora", "path": "../img/ant/pandora3.png"},
    {"key": "pandora", "path": "../img/ant/pand.png"},
    {"key": "red", "path": "../img/ant/ant_red.png"},
    {"key": "blue", "path": "../img/ant/ant_blue.png"},
    {"key": "red", "path": "../img/ant/ant_red_left.png"},
    {"key": "blue", "path": "../img/ant/ant_blue_right.png"},
    {"key": "red", "path": "../img/ant/ant_red_right.png"},
    {"key": "blue", "path": "../img/ant/blue_ant.png"},
    {"key": "red", "path": "../img/ant/name_ant_red.png"},
    {"key": "blue", "path": "../img/ant/name_ant_blue.png"},
    {"key": "red", "path": "../img/ant/red_ant.png"},
]


# STAGE_FINAL = False
STAGE_FINAL = True
ENABLE_START = False
FLY_USED = False
POSITION_VALID = False
SIDE = "a"
MAX_TURN = 9
COUNT_TURN_BLUE_ANTS = 0
COUNT_TURN_RED_ANTS = 0
COUNT_TURN_BOSS = 0


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
        result = find_image("../img/fly.png")
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
    keyboard.press_and_release("2")
    keyboard.press_and_release("4")
    keyboard.press_and_release("6")
    keyboard.press("space")
    time.sleep(0.3)
    keyboard.release("space")
    time.sleep(2)


while True:
    check = find_image("../img/ant/ants_check.png")
    if check["found"]:
        ENABLE_START = True

    for img_info in IMAGES_PATH:
        key = img_info["key"]
        result = find_image(img_info["path"])

        if result["found"]:
            x = result["position_x"]
            y = result["position_y"]
            print(f"step: '{key}' x: {x} y: {y}")

            if key == "my_turn":
                ENABLE_START = False

                for monster_info in MONSTERS_IMAGES_PATH:
                    k = monster_info["key"]
                    monster = find_image(monster_info["path"])

                    if monster["found"]:
                        x = monster["position_x"]
                        y = monster["position_y"]
                        if not STAGE_FINAL:
                            print(f"monster: '{k}' x: {x} y: {y}")
                            if k == "blue":
                                COUNT_TURN_BLUE_ANTS += 1
                                if COUNT_TURN_BLUE_ANTS < MAX_TURN:
                                    SIDE = "d"
                                    keyboard.press_and_release("d")
                                else:
                                    keyboard.press_and_release("d")
                                    fly()
                                    SIDE = "a"
                                    keyboard.press_and_release("a")
                            else:
                                COUNT_TURN_RED_ANTS += 1
                                if COUNT_TURN_RED_ANTS < MAX_TURN:
                                    SIDE = "a"
                                    keyboard.press_and_release("a")
                                else:
                                    keyboard.press_and_release("a")
                                    fly()
                                    SIDE = "d"
                                    keyboard.press_and_release("d")
                            attack_ants()
                            break
                        else:
                            if COUNT_TURN_BOSS < 3:
                                print("round_boss")
                                round_boss()
                            else:
                                print("optional_round_boss")
                                optional_round_boss()
                                
                            COUNT_TURN_BOSS += 1
                            break

            elif key == "win":
                time.sleep(5)
            elif key == "pandora_room":
                STAGE_FINAL = True
                ENABLE_START = True
            elif key == "start":
                FLY_USED = False
                COUNT_TURN_BLUE_ANTS = 0
                COUNT_TURN_RED_ANTS = 0
                COUNT_TURN_BOSS = 0
                if ENABLE_START:
                    pyautogui.click(x, y)
            elif key == "cards":
                flip_cards()
            else:
                FLY_USED = False
                COUNT_TURN_BLUE_ANTS = 0
                COUNT_TURN_RED_ANTS = 0
                COUNT_TURN_BOSS = 0
                if key == "select" or key == "selected_ant":
                    STAGE_FINAL = False
                if key == "select" or key == "selected_ant" or key == "ok":
                    ENABLE_START = False
                pyautogui.click(x, y)
                
    if COUNT_TURN_BOSS > 5:
        COUNT_TURN_BOSS = 0
    time.sleep(1)
