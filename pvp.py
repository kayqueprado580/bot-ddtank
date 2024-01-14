import pyautogui
import time
import cv2
import logging
import keyboard

from missions import found_missions_completed

logging.basicConfig(filename="log/error_log.txt", level=logging.ERROR)

TURN_ON = False
SIDE = 0

COUNT_PASS = 0
IMAGES_PASS = [
    {"key": "turn_on", "path": "img/pass.png"},
    {"key": "turn_on", "path": "img/pass2.png"},
    {"key": "turn_on", "path": "img/pass1.png"},
    {"key": "turn_on", "path": "img/pass3.png"},
    {"key": "turn_on", "path": "img/pass4.png"},
    {"key": "turn_on", "path": "img/pass5.png"},
    {"key": "turn_on", "path": "img/pass6.png"},
]


IMAGES_ROOM = [
    {"key": "room", "path": "img/games_room.png"},
]

ISCLICK_COMBAT = False
IMAGES_COMBAT = [
    {"key": "free_combat", "path": "img/free_combat.png"},
]

IMAGES_PLAY = [
    {"key": "enter_room", "path": "img/play.png"},
]

IMAGES_WAIT = [
    {"key": "wait", "path": "img/wait.png"},
]

IMAGES_READY = [
    {"key": "ready", "path": "img/ready.png"},
]

IMAGES_OK = [
    {"key": "ok", "path": "img/ok.png"},
]

IMAGES_START = [
    {"key": "start", "path": "img/btn_init.png"},
]

AVAILABLE = False
IMAGES_AVAILABLE = [
    {"key": "available", "path": "img/available.png"},
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
        error_message = f"An error occurred: {e}"
        logging.error(error_message)
        with open("log/log.txt", "a") as log_file:
            log_file.write(error_message + "\n")

    return result


def attack_trident():
    time.sleep(0.8)
    keyboard.press_and_release("1")
    time.sleep(0.8)
    keyboard.press_and_release("2")
    time.sleep(0.2)
    keyboard.press("space")
    time.sleep(0.03)
    keyboard.release("space")


def step_click(key, x, y):
    print(f"step: '{key}' x: {x} y: {y}")
    pyautogui.click(x, y)


while True:
    if not TURN_ON:
        found_missions_completed()
        
        for img_room in IMAGES_ROOM:
            room = find_image(img_room["path"])
            if room["found"]:
                step_click(img_room["key"], room["position_x"], room["position_y"])
                break

        for img_play in IMAGES_PLAY:
            play = find_image(img_play["path"])
            if play["found"]:
                step_click(img_play["key"], play["position_x"], play["position_y"])
                break

        if not ISCLICK_COMBAT:
            for img_combat in IMAGES_COMBAT:
                free_combat = find_image(img_combat["path"])
                if free_combat["found"]:
                    step_click(
                        img_combat["key"],
                        free_combat["position_x"],
                        free_combat["position_y"],
                    )
                    ISCLICK_COMBAT = True
                    break
                
        if not AVAILABLE:
            for img_ready in IMAGES_READY:
                ready = find_image(img_ready["path"])
                if ready["found"]:
                    step_click(img_ready["key"], ready["position_x"], ready["position_y"])
                    break

        for img_ok in IMAGES_OK:
            ok = find_image(img_ok["path"])
            if ok["found"]:
                step_click(img_ok["key"], ok["position_x"], ok["position_y"])
                break

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

        if not AVAILABLE:
            for img_start in IMAGES_START:
                start = find_image(img_start["path"])
                if start["found"]:
                    step_click(img_start["key"], start["position_x"], start["position_y"])
                    break

        for img_wait in IMAGES_WAIT:
            wait = find_image(img_wait["path"])
            if wait["found"]:
                COUNT_PASS = 0
                step_click(img_wait["key"], wait["position_x"], wait["position_y"])
                time.sleep(5)
                break

    for img_pass in IMAGES_PASS:
        key = img_pass["key"]
        turn_on = find_image(img_pass["path"])
        if turn_on["found"]:
                ISCLICK_COMBAT = False
                print(f"contador: {COUNT_PASS}")
                
                if COUNT_PASS < 3:
                    step = f"{key} - action: pass"
                    step_click(step, turn_on["position_x"], turn_on["position_y"])
                else:
                    step = f"{key} - action: auto attack"
                    x_aux = turn_on["position_x"] - 40
                    y_aux = turn_on["position_y"] - 80
                    step_click(step, x_aux, y_aux)
                    time.sleep(0.05)
                    if SIDE < 2:
                        print("walk right")
                        keyboard.press("d")
                        time.sleep(0.2)
                        keyboard.release("d")
                    else:
                        print("walk left")
                        keyboard.press("a")
                        time.sleep(0.2)
                        keyboard.release("a")
                        
                    if SIDE > 4:
                        SIDE = 0
                    else:
                        SIDE += 1

                    attack_trident()
                    time.sleep(2)

                if COUNT_PASS > 7:
                    COUNT_PASS = 0
                else:
                    COUNT_PASS += 1
            
                time.sleep(1)
                TURN_ON = True
                break
        else:
            TURN_ON = False

    time.sleep(0.3)
