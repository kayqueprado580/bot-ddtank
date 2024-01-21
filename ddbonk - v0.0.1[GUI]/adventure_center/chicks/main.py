import pyautogui
import time
import cv2
import logging
import keyboard
import sys

from lib import angles
from stage_1 import (
    turn_on_attack,
)

logging.basicConfig(filename="log/error_log.txt", level=logging.ERROR)


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
        with open("log/log.txt", "a") as log_file:
            log_file.write(error_message + "\n")

    return result


def step_click(key, x, y):
    print(f"step: '{key}' x: {x} y: {y}")
    pyautogui.click(x, y)


def setting_level():
    global LEVEL

    print("Selecione o nível...")
    print("Tecle: ")
    print("1 - Facil || 2 - Normal || 3 - Dificil")
    input_user = input("Digite um 1, 2 ou 3: ")

    try:
        LEVEL = int(input_user)
        if LEVEL == 1 or LEVEL == 2 or LEVEL == 2:
            level = IMAGES_LEVEL[LEVEL - 1]["key"]
            print(f"level selecionado: {level}")
        else:
            print("Erro: Por favor, digite apenas 1, 2 ou 3")
            sys.exit()

    except ValueError:
        print("Erro: Por favor, digite um valor inteiro válido.")
        sys.exit()


def setting_instance():
    global IMAGES_CHECK, IMAGES_CENTRAL, IMAGES_PLAY, IMAGES_READY, IMAGES_START, IMAGES_AVAILABLE, IMAGES_SELECTED, IMAGES_SELECT, IMAGES_OK, IMAGES_LEVEL
    global ENABLE_START, LEVEL, AVAILABLE, CHICKS_SELECTED

    check = find_image(IMAGES_CHECK[0]["path"])
    if check["found"]:
        print(f"step: checked instance")
        STAGE_1 = True
        AVAILABLE = False
        ENABLE_START = True

    for img_central in IMAGES_CENTRAL:
        central = find_image(img_central["path"])
        if central["found"]:
            step_click(img_central["key"], central["position_x"], central["position_y"])
            break

    for img_play in IMAGES_PLAY:
        play = find_image(img_play["path"])
        if play["found"]:
            step_click(img_play["key"], play["position_x"], play["position_y"])
            break

    for img_ready in IMAGES_READY:
        ready = find_image(img_ready["path"])
        if ready["found"]:
            step_click(img_ready["key"], ready["position_x"], ready["position_y"])
            break

    if CHICKS_SELECTED or ENABLE_START:
        for img_ok in IMAGES_OK:
            ok = find_image(img_ok["path"])
            if ok["found"]:
                step_click(img_ok["key"], ok["position_x"], ok["position_y"])
                time.sleep(1)
                break

    if not CHICKS_SELECTED and not ENABLE_START:
        for img_available in IMAGES_AVAILABLE:
            available = find_image(img_available["path"])
            if available["found"]:
                AVAILABLE = True
                step_click(
                    img_available["key"],
                    available["position_x"],
                    available["position_y"],
                )
                break
            else:
                AVAILABLE = False

    if not AVAILABLE and not CHICKS_SELECTED:
        for img_select in IMAGES_SELECT:
            select = find_image(img_select["path"])
            if select["found"]:
                step_click(
                    img_select["key"], select["position_x"], select["position_y"]
                )
                break

    if not AVAILABLE and not ENABLE_START:
        for img_selected in IMAGES_SELECTED:
            selected = find_image(img_selected["path"])
            if selected["found"]:
                step_click(
                    img_selected["key"], selected["position_x"], selected["position_y"]
                )
                CHICKS_SELECTED = True
                STAGE_1 = True
                break

    if CHICKS_SELECTED:
        level = find_image(IMAGES_LEVEL[LEVEL - 1]["path"])
        if level["found"]:
            step_click(
                IMAGES_LEVEL[LEVEL - 1]["key"],
                level["position_x"],
                level["position_y"],
            )

    if not AVAILABLE and ENABLE_START:
        for img_start in IMAGES_START:
            start = find_image(img_start["path"])
            if start["found"]:
                step_click(img_start["key"], start["position_x"], start["position_y"])
                break


def manager_turn():
    global STAGE_1

    x_aux = turn_on["position_x"] - 40
    y_aux = turn_on["position_y"] - 80
    step_click(key, x_aux, y_aux)
    time.sleep(0.05)

    turn_on_attack()

    # if STAGE_1:
    # elif STAGE_2:
    # print("fazer ainda")
    # else:
    # print("fazer ainda2")


IMAGES_CENTRAL = [{"key": "room", "path": "img/central.png"}]
IMAGES_PLAY = [{"key": "enter_room", "path": "img/play.png"}]
IMAGES_READY = [{"key": "ready", "path": "img/ready.png"}]
IMAGES_OK = [{"key": "ok", "path": "img/ok.png"}]
IMAGES_START = [{"key": "start", "path": "img/start.png"}]
IMAGES_AVAILABLE = [{"key": "available", "path": "img/available.png"}]
IMAGES_CHECK = [{"key": "check", "path": "img/check.png"}]
IMAGES_SELECTED = [{"key": "selected_chicks", "path": "img/selected.png"}]
IMAGES_SELECT = [{"key": "select", "path": "img/select.png"}]
IMAGES_LEVEL = [
    {"key": "easy", "path": "img/easy.png"},
    {"key": "normal", "path": "img/normal.png"},
]

STAGE_1 = False
STAGE_2 = False
STAGE_3 = False
AVAILABLE = True
TURN_ON = False
CHICKS_SELECTED = False
ENABLE_START = False
LEVEL = 1

while True:
    if not TURN_ON:
        setting_instance()

    for img_pass in angles.IMAGES_PASS:
        key = img_pass["key"]
        turn_on = find_image(img_pass["path"])
        if turn_on["found"]:
            TURN_ON = True
            ENABLE_START = False
            manager_turn()
            break
        else:
            TURN_ON = False

    time.sleep(0.3)
