import pyautogui
import time
import cv2
import keyboard
import numpy as np
import ctypes
from PIL import Image

POSITION_VALID = False
POSX = 0
POSY = 0
ANGLE = 0
X = 1


def attack_boss():
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


def optional_round_boss():
    global X, POSITION_VALID, POSX, POSY
    map_off_location = pyautogui.locateCenterOnScreen(
        "../img/ant/mapOff.png", confidence=0.9
    )
    if map_off_location is not None:
        x1, y1 = int(map_off_location.x - 190), int(map_off_location.y - 7)
        x2, y2 = int(map_off_location.x + 15), int(map_off_location.y + 130)

        screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        screenshot.save("../img/ant/map.png")
        image = cv2.imread("../img/ant/map.png")

        # Define the desired blue color (in BGR format)
        blue_color = np.array([213, 6, 7], dtype=np.uint8)

        # Initialize the coordinates of the nearest point
        nearest_point = None
        smallest_distance = float("inf")  # Initialized with a very large value

        # Iterate through all pixels in the image to find the nearest point
        for x in range(image.shape[1]):
            for y in range(image.shape[0]):
                pixel = image[y, x]

                # Calculate the Euclidean distance from the pixel color to the blue color
                distance = np.linalg.norm(pixel - blue_color)

                # Check if the distance is smaller than the current smallest distance
                if distance < smallest_distance:
                    smallest_distance = distance
                    nearest_point = (x, y)

        # If a blue point was found in the image
        if nearest_point is not None:
            x, y = nearest_point

            # Make a copy of the original image to draw the line
            image_with_line = image.copy()

            # Draw a yellow line at the nearest point
            cv2.line(image_with_line, (x, y), (x, y), (0, 255, 255), thickness=2)

            # Save the image with the yellow line
            cv2.imwrite("../img/ant/line.png", image_with_line)

            POSX = x
            POSY = y
            POSITION_VALID = True
            print(f"Nearest point to blue at coordinates (x, y): ({x}, {y})")
            print(f"Distance to blue: {smallest_distance}")
        else:
            print("No blue point found in the image.")

    if POSITION_VALID:
        print(f"POSX: {POSX} - POSY:{POSY}")
        if POSX < 15:
            print("position 1")

            while X < (28 - ANGLE):
                keyboard.press_and_release("w")
                X += 1
            attack_boss()
            keyboard.press("space")
            time.sleep(2.2)
            keyboard.release("space")

        elif 15 <= POSX < 30:
            print("position 2")

            while X < (24 - ANGLE):
                keyboard.press_and_release("w")
                X += 1
            attack_boss()
            keyboard.press("space")
            time.sleep(2.1)
            keyboard.release("space")

        elif 30 <= POSX < 40:
            print("position 3")

            attack_boss()
            keyboard.press("space")
            time.sleep(1.9)
            keyboard.release("space")

        else:
            print("position 4")

            while X < (39 - ANGLE):
                print(f"x: {x}")
                keyboard.press_and_release("w")
                X += 1
            attack_boss()
            keyboard.press("space")
            time.sleep(1.9)
            keyboard.release("space")
        time.sleep(3)
