import pyautogui
import time
import cv2
import logging
import keyboard

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
