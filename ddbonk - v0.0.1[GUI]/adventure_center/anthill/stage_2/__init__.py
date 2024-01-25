import pyautogui
import time
import cv2
import keyboard

from lib import turn_on


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

adjusted_angle = False
key = 0


def find_angle(image_path, confidence=0.9):
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
        pass

    return result


def adjust_angle(max):
    global adjusted_angle
    time.sleep(0.2)

    if not adjusted_angle:
        print("adjusting angle...")
        i = 0
        while i < max:
            keyboard.press_and_release("w")
            time.sleep(0.07)
            i += 1
        adjusted_angle = True


def take_force(key):
    force = 2.5
    if key == "41":
        force = 1.9
    elif key == "46":
        force = 1.5
    elif key == "47":
        force = 1.4
    elif key == "51":
        force = 1.2
    else:
        force = 2.2

    return force


def take_angles(key):
    if key == "-5":
        adjust_angle(33)
    elif key == "0":
        adjust_angle(29)
    elif key == "6" or key == "7":
        adjust_angle(24)
    elif key == "10" or key == "11" or key == "12":
        adjust_angle(20)
    elif key == "13" or key == "14" or key == "15":
        adjust_angle(18)
    elif key == "16" or key == "17" or key == "19":
        adjust_angle(16)


def turn_on_boss_stage_2():
    global adjusted_angle, key

    count = 0
    force = 2.5
    number_attempts = len(turn_on.ANGLES_IMAGES_PATH) * 2

    if not adjusted_angle:
        for angle in turn_on.ANGLES_IMAGES_PATH:
            key = angle["key"]
            ang = find_angle(angle["path"])
            if ang["found"]:
                print(f"angle: '{key}'")
                time.sleep(0.1)
                take_angles(key)
                force = take_force(key)
                break
            else:
                print(
                    f"attempt counter to get the angle: {count} of max try: {number_attempts}"
                )
                if count >= int(number_attempts):
                    print(f"not found angle")
                    time.sleep(5)
                    count = 0
                    break
                else:
                    count += 1
    else:
        force = take_force(key)

    time.sleep(0.5)
    turn_on.use_skills_attack()
    time.sleep(0.5)
    turn_on.attack(force)
    time.sleep(6)


def reset_parameters_default():
    global adjusted_angle, key
    adjusted_angle = False
    key = 0
