import time

from lib import turnon

# SETTINGS TURN
ADJUSTED_ANGLE = False
FORCE = 3


def set_default_parameters_house_chickens_3():
    global ADJUSTED_ANGLE, FORCE
    FORCE = 3
    ADJUSTED_ANGLE = False


def house_chickens_3_turn_on():
    global FORCE
    take_angle_force()
    print("step: attack house chickens")

    turnon.use_skills_attack()
    turnon.attack(FORCE)
    time.sleep(10)


def take_angle_force():
    global ADJUSTED_ANGLE, FORCE
    print("step: take angle...")
    time.sleep(1)

    if not ADJUSTED_ANGLE:
        for angle in turnon.IMAGES_ANGLES:
            key = angle["key"]
            result = turnon.get_angle(angle["path"])
            if result["found"]:
                print(f"angle: '{key}'")
                change_angle(key)
                time.sleep(0.1)
                FORCE = get_force(key)
                time.sleep(0.1)
                ADJUSTED_ANGLE = True
                break


def change_angle(angle):
    if angle == "-5":
        turnon.adjust_angle(35)
    elif angle == "0":
        turnon.adjust_angle(30)
    elif angle == "6":
        turnon.adjust_angle(24)
    elif angle == "7":
        turnon.adjust_angle(23)
    elif angle == "10":
        turnon.adjust_angle(20)
    elif angle == "11":
        turnon.adjust_angle(19)
    elif angle == "12":
        turnon.adjust_angle(18)
    elif angle == "13":
        turnon.adjust_angle(17)
    elif angle == "14":
        turnon.adjust_angle(16)
    elif angle == "15":
        turnon.adjust_angle1(5)
    elif angle == "16":
        turnon.adjust_angle(14)
    elif angle == "17":
        turnon.adjust_angle(13)
    elif angle == "19":
        turnon.adjust_angle(11)
    elif angle == "20":
        turnon.adjust_angle(10)
    elif angle == "21":
        turnon.adjust_angle(9)
    elif angle == "23":
        turnon.adjust_angle(7)
    elif angle == "25":
        turnon.adjust_angle(5)
    elif angle == "26":
        turnon.adjust_angle(4)


def get_force(angle):
    force = 3
    if angle == "33":
        force = 2.3
    elif angle == "41":
        force = 2.0
    elif angle == "46":
        force = 1.8
    elif angle == "50" or angle == "51":
        force = 1.4
    else:
        force = 2.5
    return force
