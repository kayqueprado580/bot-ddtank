import pyautogui
import time
import cv2
import logging
import keyboard

logging.basicConfig(filename="log/error_log.txt", level=logging.ERROR)

IMAGES_PATH = [
    {"key": "room", "path": "img/games_room.png"},
    {"key": "play", "path": "img/play.png"},
    {"key": "ready", "path": "img/ready.png"},
    {"key": "wait", "path": "img/wait.png"},
    {"key": "pass", "path": "img/pass.png"},
    {"key": "pass", "path": "img/pass2.png"},
    {"key": "ok", "path": "img/ok.png"},
    {"key": "init", "path": "img/btn_init.png"},
    # {"key": "init", "path": "img/start_game.png"},
    # {"key": "quest", "path": "img/quest.png"},
]

IMAGES_QUEST_PATH = [
    {"key": "collect_reward", "path": "img/collect_reward.png"},
    {"key": "daily_contri", "path": "img/daily_contri.png"},
    {"key": "daily_contri_out", "path": "img/daily_contri_out.png"},
    {"key": "daily_hole_in", "path": "img/daily_hole_in.png"},
    {"key": "daily_hole_out", "path": "img/daily_hole_out.png"},
    # {"key": "close", "path": "img/btn_close.png"},
]

COUNT_PASS = 0


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


def auto_attack():
    time.sleep(0.8)
    keyboard.press_and_release("1")
    time.sleep(0.8)
    keyboard.press_and_release("2")
    keyboard.press("space")
    time.sleep(0.02)
    keyboard.release("space")


while True:
    for img_info in IMAGES_PATH:
        key = img_info["key"]
        path = img_info["path"]
        result = find_image(path)

        if result["found"]:
            x = result["position_x"]
            y = result["position_y"]
            print(f"step: '{key}' x: {x} y: {y}")
            if key == "wait":
                time.sleep(10)
            elif key == "pass":
                print(f"COUNT_PASS: '{COUNT_PASS}'")
                if COUNT_PASS > 7:
                    COUNT_PASS = 0
                else:
                    COUNT_PASS += 1

                # até 3
                if COUNT_PASS < 4:
                    pyautogui.click(result["position_x"], result["position_y"])
                else:
                    print("autoattack")
                    x_aux = x - 40
                    y_aux = y - 80
                    pyautogui.click(x_aux, y_aux)
                    time.sleep(0.3)

                    if COUNT_PASS > 3 and COUNT_PASS < 6:
                        print("walk ->")
                        i = 0
                        while i < 10:
                            keyboard.press_and_release("d")
                            time.sleep(0.1)
                            i += 1

                    if COUNT_PASS > 6:
                        print("walk <-")
                        i = 0
                        while i < 10:
                            keyboard.press_and_release("a")
                            time.sleep(0.1)
                            i += 1

                    auto_attack()
                    break
                break
            else:
                COUNT_PASS = 0
                pyautogui.click(result["position_x"], result["position_y"])

            break

    time.sleep(0.5)
