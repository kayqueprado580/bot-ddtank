import pyautogui
import time
import cv2
import logging
import keyboard

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
    time.sleep(0.035)
    keyboard.release("space")


def step_click(key, x, y):
    print(f"step: '{key}' x: {x} y: {y}")
    pyautogui.click(x, y)


def found_missions_completed():
    IMAGES_QUEST = [
        {"key": "quest", "path": "img/quest2.png"},
        {"key": "quest", "path": "img/quest3.png"},
    ]

    rewards = False
    no_more = False
    aux_flag = False

    i = 0
    while i < 3:
        for img_quest in IMAGES_QUEST:
            key = img_quest["key"]
            quest = find_image(img_quest["path"])

            if quest["found"]:
                x = quest["position_x"]
                y = quest["position_y"]
                print(f"step: '{key}' x: {x} y: {y}")
                pyautogui.click(x, y)
                time.sleep(0.1)
                rewards = True
                break
        time.sleep(0.5)
        i += 1

    if i >= 2:
        no_more = True

    if rewards:
        aux_flag = exec_collection()

    if aux_flag or no_more:
        close = find_image("img/btn_close.png")
        if close["found"]:
            x = close["position_x"] + 20
            y = close["position_y"] + 10
            print(f"step: 'close' x: {x} y: {y}")
            pyautogui.click(x, y)
            rewards = False
            no_more = False


def exec_collection():
    IMAGES_QUEST_COMPLETED = [
        {"key": "completed_mission", "path": "img/completed_mission.png"},
        {"key": "completed_mission", "path": "img/completed_mission1.png"},
        {"key": "completed_mission", "path": "img/completed_mission2.png"},
    ]

    COMPLETED = False
    COLLECT = False
    i = 0
    no_more = False
    while i < 3:
        found_any_image = False

        for img_completed in IMAGES_QUEST_COMPLETED:
            key = img_completed["key"]
            completed = find_image(img_completed["path"])

            if completed["found"]:
                x = completed["position_x"]
                y = completed["position_y"]
                print(f"step: '{key}' x: {x} y: {y}")
                pyautogui.click(x, y)
                time.sleep(0.1)
                COMPLETED = True
                found_any_image = True
                break
            else:
                COMPLETED = False
                COLLECT = False

        if COMPLETED:
            collect = find_image("img/collect_reward.png")
            if collect["found"]:
                x = collect["position_x"]
                y = collect["position_y"]
                print(f"step: 'collect' x: {x} y: {y}")
                pyautogui.click(x, y)
                time.sleep(0.1)
                COLLECT = True
                COMPLETED = False
                found_any_image = True
            else:
                COLLECT = False

        time.sleep(0.5)
        i += 1
        if not found_any_image:
            no_more = True

    return no_more


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
            print(f"contador: {COUNT_PASS}")
            if COUNT_PASS < 7:
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
                time.sleep(4)

            if COUNT_PASS > 20:
                COUNT_PASS = 0
            else:
                COUNT_PASS += 1

            time.sleep(1)
            TURN_ON = True
            break
        else:
            TURN_ON = False

    time.sleep(0.5)
