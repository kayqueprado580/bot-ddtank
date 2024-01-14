import pyautogui
import time
import cv2
import logging

logging.basicConfig(filename="log/error_log.txt", level=logging.ERROR)


IMAGES_QUEST = [
    {"key": "quest", "path": "img/quest2.png"},
    {"key": "quest", "path": "img/quest3.png"},
]

IMAGES_QUEST_COMPLETED = [
    {"key": "completed_mission", "path": "img/completed_mission.png"},
    {"key": "completed_mission", "path": "img/completed_mission1.png"},
    {"key": "completed_mission", "path": "img/completed_mission2.png"},
]

# IMAGE_COLLECT_REWARDS = {"key": "collect", "path": "img/collect_reward.png"}
# IMAGE_CLOSE = {"key": "close", "path": "img/btn_close.png"}

REWARDS = True
COMPLETED = False
COLLECT = False
CLOSE = False


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


while True:
    for img_quest in IMAGES_QUEST:
        key = img_quest["key"]
        quest = find_image(img_quest["path"])

        if quest["found"]:
            x = quest["position_x"]
            y = quest["position_y"]
            print(f"step: '{key}' x: {x} y: {y}")
            pyautogui.click(x, y)
            time.sleep(0.1)
            REWARDS = True
            CLOSE = False
            break

    if REWARDS:
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
                CLOSE = True

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
            CLOSE = True

    if CLOSE and (not COMPLETED and not COLLECT):
        close = find_image("img/btn_close.png")
        if close["found"]:
            x = close["position_x"] + 20
            y = close["position_y"] + 10
            print(f"step: 'close' x: {x} y: {y}")
            pyautogui.click(x, y)
            REWARDS = False
            CLOSE = False

    time.sleep(0.5)
