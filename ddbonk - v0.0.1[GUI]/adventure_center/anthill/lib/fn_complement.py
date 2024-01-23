import cv2
import pyautogui


def find(image_path, confidence=0.8):
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


def click(key, x, y):
    print(f"step: '{key}' x: {x} y: {y}")
    pyautogui.click(x, y)
