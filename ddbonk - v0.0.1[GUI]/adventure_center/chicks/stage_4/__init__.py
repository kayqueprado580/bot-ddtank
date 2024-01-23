import time
import pyautogui
import cv2

from lib import turnon

# SETTINGS TURN
ADJUSTED_ANGLE = False
FORCE = 3

IMAGES_DONKEY_CHICKEN_LIVE = [
    {"key": "live", "path": "img/stage_4/burrinho_1.png"},
    {"key": "live", "path": "img/stage_4/live_burrinho.png"},
]

IMAGES_DONKEY_CHICKEN_DEAD = [
    {"key": "dead", "path": "img/stage_4/dead_burrinho.png"},
    {"key": "dead", "path": "img/stage_4/burrinho_dead.png"},
]


def find_image(image_path, confidence=0.8):
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


def check_donkey_chicken_is_alive():
    donkey_chicken_alive = True
    global IMAGES_DONKEY_CHICKEN_DEAD, IMAGES_DONKEY_CHICKEN_LIVE
    for img_live in IMAGES_DONKEY_CHICKEN_LIVE:
        live = find_image(img_live["path"])
        if live["found"]:
            donkey_chicken_alive = True
            print("step: donkey chicken is alive")
            break

    for img_dead in IMAGES_DONKEY_CHICKEN_DEAD:
        dead = find_image(img_dead["path"])
        if dead["found"]:
            donkey_chicken_alive = False
            print("step: donkey chicken is dead")
            break
    return donkey_chicken_alive


def donkey_chicken_4_turn_on():
    global FORCE
    chicken_alive = check_donkey_chicken_is_alive()

    if chicken_alive:
        take_angle_force()
        print("step: attack donkey chicken")
    else:
        print("step: attack trapped chicks")
        turnon.walking_right()
        turnon.adjust_angle(10)
        FORCE = 1.8

    turnon.use_skills_attack()
    turnon.attack(FORCE)
    time.sleep(10)


def take_angle_force():
    global ADJUSTED_ANGLE, FORCE
    print("step: take angle...")
    time.sleep(1)

    if not ADJUSTED_ANGLE:
        for angle in turnon.IMAGES_ANGLES:
            key = angle["key"]
            result = turnon.get_angle(angle["path"])
            if result["found"]:
                print(f"angle: '{key}'")
                change_angle(key)
                time.sleep(0.1)
                FORCE = get_force(key)
                time.sleep(0.1)
                ADJUSTED_ANGLE = True
                break


def change_angle(angle):
    if angle == "-5":
        turnon.adjust_angle(25)
    elif angle == "0":
        turnon.adjust_angle(20)
    elif angle == "6":
        turnon.adjust_angle(14)
    elif angle == "7":
        turnon.adjust_angle(13)
    elif angle == "10":
        turnon.adjust_angle(10)
    elif angle == "11":
        turnon.adjust_angle(9)
    elif angle == "12":
        turnon.adjust_angle(8)
    elif angle == "13":
        turnon.adjust_angle(7)
    elif angle == "14":
        turnon.adjust_angle(6)
    elif angle == "15":
        turnon.adjust_angle(5)
    elif angle == "16":
        turnon.adjust_angle(4)
    elif angle == "17":
        turnon.adjust_angle(3)
    elif angle == "19":
        turnon.adjust_angle(1)


def get_force(angle):
    force = 3
    if angle == "26" or angle == "30" or angle == "33":
        force = 1.8
    elif angle == "41":
        force = 1.5
    elif angle == "46" or angle == "50" or angle == "51":
        force = 1.2
    else:
        force = 2.1
    return force


def set_default_parameters_donkey_chicken_4():
    global ADJUSTED_ANGLE, FORCE
    FORCE = 3
    ADJUSTED_ANGLE = False
