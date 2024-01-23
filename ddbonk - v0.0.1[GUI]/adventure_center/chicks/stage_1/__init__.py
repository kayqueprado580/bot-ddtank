import pyautogui
import time
import cv2
import keyboard

# SETTINGS TURN
FLY_USED = False
GET_SIDE = False
SIDE = 0  # SIDE 0 = RIGHT | SIDE 1 = LEFT
COUNT_TURN = 0
MAX_TURN = 20
MAX_TURN_BASE = 20

IMAGES_LEFT = [
    {"key": "left", "path": "img/stage_1/side_left.png"},
    {"key": "left", "path": "img/stage_1/side_left_1.png"},
    {"key": "left", "path": "img/stage_1/side_left_2.png"},
]

IMAGES_RIGHT = [
    {"key": "right", "path": "img/stage_1/side_right.png"},
    {"key": "right", "path": "img/stage_1/side_right_1.png"},
    {"key": "right", "path": "img/stage_1/side_right_2.png"},
    {"key": "right", "path": "img/stage_1/side_right_3.png"},
]

IMAGE_CHICK = {"key": "chick", "path": "img/stage_1/chicks.png"}


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
        pass

    return result


def set_default_parameters():
    global GET_SIDE, SIDE, FLY_USED, COUNT_TURN, MAX_TURN, MAX_TURN_BASE
    GET_SIDE = False
    FLY_USED = False
    SIDE = 0
    COUNT_TURN = 0
    MAX_TURN = MAX_TURN_BASE


def fly():
    global FLY_USED
    if not FLY_USED:
        print("use fly...")
        result = find_image("img/fly.png")
        if result["found"]:
            pyautogui.click(result["position_x"], result["position_y"])
            keyboard.press_and_release("f")
            keyboard.press("space")
            time.sleep(0.8)
            keyboard.release("space")
            time.sleep(2)
            FLY_USED = True


def attack():
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
    time.sleep(5)


def walking():
    global SIDE, FLY_USED

    if FLY_USED:
        if SIDE == 1:
            SIDE = 0
        else:
            SIDE = 1

    if SIDE == 1:
        print("walking left")
        keyboard.press("a")
        time.sleep(1)
        keyboard.release("a")
    else:
        print("walking right")
        keyboard.press("d")
        time.sleep(1)
        keyboard.release("d")


def look_left():
    global GET_SIDE, IMAGES_LEFT, SIDE
    for img in IMAGES_LEFT:
        left = find_image(img["path"])
        if left["found"] and not GET_SIDE:
            print("born on the left")
            SIDE = 0
            GET_SIDE = True
            break


def look_right():
    global GET_SIDE, IMAGES_RIGHT, SIDE
    for img in IMAGES_RIGHT:
        right = find_image(img["path"])
        if right["found"] and not GET_SIDE:
            print("born on the right")
            SIDE = 1
            GET_SIDE = True
            break


def chicks_1_turn_on():
    global GET_SIDE, COUNT_TURN, MAX_TURN, FLY_USED
    count = 0

    if not GET_SIDE:
        look_left()

    if not GET_SIDE:
        look_right()

    if GET_SIDE:
        if COUNT_TURN < MAX_TURN:
            if COUNT_TURN < 2 and not FLY_USED:
                walking()
            attack()
            time.sleep(3)
            COUNT_TURN += 1
        else:
            COUNT_TURN = 0
            walking()
            fly()

    count += 1
    time.sleep(0.2)
