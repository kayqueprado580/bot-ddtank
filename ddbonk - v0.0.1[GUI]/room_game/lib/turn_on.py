import time
import keyboard
from fn_complement import *


IMAGES_PASS = [
    "../img/pass.png",
    "../img/pass1.png",
    "../img/pass2.png",
    "../img/pass3.png",
    "../img/pass4.png",
    "../img/pass5.png",
    "../img/pass6.png",
]


def click_for_attack(x, y):
    click("my turn - action: click", (x - 40), (y - 80))


def pass_turn(x, y):
    click("my turn - action: pass", x, y)


def use_skills_trident():
    print("step: my turn - action: use skills trident attack")
    time.sleep(0.8)
    keyboard.press_and_release("1")
    time.sleep(0.8)
    keyboard.press_and_release("2")
    time.sleep(0.2)


def use_skills_attack():
    print("step: my turn - action: use alternative skills of attack")
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
    print("step: my turn - action: attack")
    keyboard.press("space")
    time.sleep(float(duration))
    keyboard.release("space")


def walking_right():
    print("step: my turn - action: walking right")
    keyboard.press("d")
    time.sleep(0.5)
    keyboard.release("d")


def walking_left():
    print("step: my turn - action: walking left")
    keyboard.press("a")
    time.sleep(0.5)
    keyboard.release("a")


# SIDE 0 = RIGHT | SIDE 1 = LEFT
def change_side(side):
    print("step: my turn - action: changed side")

    if side == 1:
        keyboard.press("d")
        time.sleep(0.2)
        keyboard.release("d")
    else:
        keyboard.press("a")
        time.sleep(0.2)
        keyboard.release("a")
