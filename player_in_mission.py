import pyautogui
import time
import cv2
import logging

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


IMAGES_QUEST_COMPLETED = [
    {"key": "completed_mission", "path": "img/completed_mission.png"},
    {"key": "completed_mission", "path": "img/completed_mission1.png"},
    {"key": "completed_mission", "path": "img/completed_mission2.png"},
]

def exec_quest():
    COMPLETED = False
    COLLECT = False
    i = 0
    no_more = False
    while i < 3:
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
            else:
                COLLECT = False

        time.sleep(0.5)
        i += 1
        if i >= 2:
            no_more = True

    return no_more
