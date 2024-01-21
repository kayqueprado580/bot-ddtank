import cv2
import pyautogui
import numpy as np
import time

# Function to find the card on the screen
def find_card(template):
    # Take a screenshot of the screen and convert it to a valid OpenCV image
    screen = np.array(pyautogui.screenshot())
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    
    # Use the cv2.matchTemplate function to find the card
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # Determine the position of the found card
    x, y = max_loc

    return x, y

def flip_cards():
    # Load the reference image of the card
    reference_card = cv2.imread('card.png')

    # Loop to find and click on the first three cards
    clicked_cards = 0
    while clicked_cards < 3:

        # Take a screenshot of the screen and find the card
        x, y = find_card(reference_card)

        # Click at the position where the card was found
        pyautogui.click(x + 50, y + 50)
        clicked_cards += 1
        time.sleep(0.8)

    # After clicking on the first three cards, exit the loop
