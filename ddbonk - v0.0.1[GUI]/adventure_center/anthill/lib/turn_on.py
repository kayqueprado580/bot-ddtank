import time
import keyboard
from lib import fn_complement

IMAGE_FLY = "img/fly.png"

IMAGES_PASS = [
    "img/pass.png",
    "img/pass1.png",
    "img/pass2.png",
    "img/pass3.png",
    "img/pass4.png",
    "img/pass5.png",
    "img/pass6.png",
]

ANGLES_IMAGES_PATH = [
    {"key": "-5", "path": "img/ang/ang_-5.png"},
    {"key": "6", "path": "img/ang/ang_6.png"},
    {"key": "10", "path": "img/ang/ang_10.png"},
    {"key": "11", "path": "img/ang/ang_11.png"},
    {"key": "12", "path": "img/ang/ang_12.png"},
    {"key": "13", "path": "img/ang/ang_13.png"},
    {"key": "14", "path": "img/ang/ang_14.png"},
    {"key": "15", "path": "img/ang/ang_15.png"},
    {"key": "16", "path": "img/ang/ang_16.png"},
    {"key": "17", "path": "img/ang/ang_17.png"},
    {"key": "19", "path": "img/ang/ang_19.png"},
    {"key": "30", "path": "img/ang/ang_30.png"},
    {"key": "41", "path": "img/ang/ang_41.png"},
    {"key": "46", "path": "img/ang/ang_46.png"},
    {"key": "51", "path": "img/ang/ang_51.png"},
    {"key": "-5", "path": "img/ang/-5.png"},
    {"key": "6", "path": "img/ang/6.png"},
    {"key": "6", "path": "img/ang/ang_6_1.png"},
    {"key": "10", "path": "img/ang/10.png"},
    {"key": "10", "path": "img/ang/10_1.png"},
    {"key": "17", "path": "img/ang/17.png"},
    {"key": "41", "path": "img/ang/41.png"},
    {"key": "46", "path": "img/ang/46.png"},
    {"key": "10", "path": "img/ang/ang_10_1.png"},
    {"key": "10", "path": "img/ang/ang_10_2.png"},
    {"key": "10", "path": "img/ang/ang_10_2.png"},
    {"key": "7", "path": "img/ang/ang_7.png"},
    {"key": "0", "path": "img/ang/ang_0.png"},
]


def click_for_attack(x, y):
    fn_complement.click("my turn - action: click", (x - 40), (y - 80))

def use_skills_trident():
    print("step: my turn - action: use skills trident attack")
    time.sleep(0.4)
    keyboard.press_and_release("2")
    time.sleep(0.3)
    keyboard.press_and_release("4")
    time.sleep(0.2)
    keyboard.press_and_release("7")
    time.sleep(0.1)


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
    time.sleep(0.2)
    keyboard.release("d")


def walking_left():
    print("step: my turn - action: walking left")
    keyboard.press("a")
    time.sleep(0.2)
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


def use_fly():
    global IMAGE_FLY
    fly = fn_complement.find(IMAGE_FLY)
    if fly["found"]:
        fn_complement.click(
            "my turn - action: use fly", fly["position_x"], fly["position_y"]
        )
        keyboard.press_and_release("f")
        keyboard.press("space")
        time.sleep(0.9)
        keyboard.release("space")
        time.sleep(3)
