import time
import keyboard
import cv2

IMAGES_PASS = [
    {"key": "turn_on", "path": "img/pass.png"},
    {"key": "turn_on", "path": "img/pass2.png"},
    {"key": "turn_on", "path": "img/pass1.png"},
    {"key": "turn_on", "path": "img/pass3.png"},
    {"key": "turn_on", "path": "img/pass4.png"},
    {"key": "turn_on", "path": "img/pass5.png"},
    {"key": "turn_on", "path": "img/pass6.png"},
]


IMAGES_ANGLES = [
    {"key": "15", "path": "img/ang/15.png"},
    {"key": "23", "path": "img/ang/23.png"},
    {"key": "-5", "path": "img/ang/-5.png"},
    {"key": "6", "path": "img/ang/6.png"},
    {"key": "10", "path": "img/ang/10.png"},
    {"key": "10_1", "path": "img/ang/10_1.png"},
    {"key": "17", "path": "img/ang/17.png"},
    {"key": "41", "path": "img/ang/41.png"},
    {"key": "46", "path": "img/ang/46.png"},
    {"key": "0", "path": "img/ang/ang_0.png"},
    {"key": "0", "path": "img/ang/ang_0_1.png"},
    {"key": "-5", "path": "img/ang/ang_-5.png"},
    {"key": "6", "path": "img/ang/ang_6.png"},
    {"key": "6", "path": "img/ang/ang_6_1.png"},
    {"key": "6", "path": "img/ang/ang_6_2.png"},
    {"key": "7", "path": "img/ang/ang_7.png"},
    {"key": "10", "path": "img/ang/ang_10.png"},
    {"key": "10", "path": "img/ang/ang_10_1.png"},
    {"key": "10", "path": "img/ang/ang_10_2.png"},
    {"key": "11", "path": "img/ang/ang_11.png"},
    {"key": "11", "path": "img/ang/ang_11_1.png"},
    {"key": "11", "path": "img/ang/ang_11_2.png"},
    {"key": "12", "path": "img/ang/ang_12.png"},
    {"key": "13", "path": "img/ang/ang_13.png"},
    {"key": "14", "path": "img/ang/ang_14.png"},
    {"key": "15", "path": "img/ang/ang_15.png"},
    {"key": "15", "path": "img/ang/ang_15_1.png"},
    {"key": "16", "path": "img/ang/ang_16.png"},
    {"key": "17", "path": "img/ang/ang_17.png"},
    {"key": "19", "path": "img/ang/ang_19.png"},
    {"key": "19", "path": "img/ang/ang_19_1.png"},
    {"key": "20", "path": "img/ang/ang_20.png"},
    {"key": "21", "path": "img/ang/ang_21.png"},
    {"key": "21", "path": "img/ang/ang_21_1.png"},
    {"key": "21", "path": "img/ang/ang_21_2.png"},
    {"key": "23", "path": "img/ang/ang_23.png"},
    {"key": "23", "path": "img/ang/ang_23_1.png"},
    {"key": "25", "path": "img/ang/ang_25.png"},
    {"key": "26", "path": "img/ang/ang_26.png"},
    {"key": "30", "path": "img/ang/ang_30.png"},
    {"key": "33", "path": "img/ang/ang_33.png"},
    {"key": "41", "path": "img/ang/ang_41.png"},
    {"key": "41", "path": "img/ang/ang_41_1.png"},
    {"key": "46", "path": "img/ang/ang_46.png"},
    {"key": "51", "path": "img/ang/ang_51.png"},
    {"key": "23", "path": "img/ang/ang_23_2.png"},
]


def get_angle(image_path, confidence=0.9):
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
    print("adjusting angle...")
    i = 0
    while i < max:
        keyboard.press_and_release("w")
        time.sleep(0.05)
        i += 1


def use_skills_attack():
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


def attack(duration):
    keyboard.press("space")
    time.sleep(float(duration))
    keyboard.release("space")


def walking_right():
    print("walking right")
    keyboard.press("d")
    time.sleep(0.5)
    keyboard.release("d")


def walking_left():
    print("walking left")
    keyboard.press("a")
    time.sleep(0.5)
    keyboard.release("a")
