import time

from lib import turnon

# SETTINGS TURN
COUNT_TURN = 0
ADJUSTED_ANGLE = False
FORCE = 3
FAT_CHICKEN = 1
BEFORE_FAT_CHICKEN = FAT_CHICKEN


def set_default_parameters_fat_chicken_2():
    global COUNT_TURN, ADJUSTED_ANGLE, FORCE, FAT_CHICKEN, BEFORE_FAT_CHICKEN
    FORCE = 3
    FAT_CHICKEN = 1
    COUNT_TURN = 0
    BEFORE_FAT_CHICKEN = FAT_CHICKEN
    ADJUSTED_ANGLE = False


def fat_chicken_2_turn_on():
    global COUNT_TURN, FAT_CHICKEN, BEFORE_FAT_CHICKEN, ADJUSTED_ANGLE, KEY
    if COUNT_TURN == 1:
        print("step: first fat chicken")
        FAT_CHICKEN = 1
        BEFORE_FAT_CHICKEN = FAT_CHICKEN
    elif COUNT_TURN == 2:
        print("step: second fat chicken")
        FAT_CHICKEN = 2
        if BEFORE_FAT_CHICKEN == 1:
            set_default_variables_attack(2)
    elif COUNT_TURN == 3:
        print("step: third fat chicken")
        FAT_CHICKEN = 3
        if BEFORE_FAT_CHICKEN == 2:
            set_default_variables_attack(3)

    attack_fat_chicken(FAT_CHICKEN)
    if COUNT_TURN >= 3:
        COUNT_TURN = 0
    else:
        COUNT_TURN += 1


def set_default_variables_attack(fat_chicken):
    global ADJUSTED_ANGLE, BEFORE_FAT_CHICKEN
    ADJUSTED_ANGLE = False
    BEFORE_FAT_CHICKEN = fat_chicken


def attack_fat_chicken(fat_chicken):
    global ADJUSTED_ANGLE, FORCE
    time.sleep(1)
    print("step: fat chicken attack...")
    if not ADJUSTED_ANGLE:
        print("step: take angle")
        for angle in turnon.IMAGES_ANGLES:
            print(f"angle: {angle}")
            key = angle["key"]
            result = turnon.get_angle(angle["path"])
            if result["found"]:
                print(f"angle: '{key}'")
                change_angle(key, fat_chicken)
                time.sleep(0.1)
                FORCE = get_force(key, fat_chicken)
                time.sleep(0.1)
                ADJUSTED_ANGLE = True
                break
    turnon.use_skills_attack()
    turnon.attack(FORCE)
    time.sleep(10)


def change_angle(angle, fat_chicken):
    if angle == "-5":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(35)
        elif fat_chicken == 3:
            turnon.adjust_angle(55)
    elif angle == "0":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(30)
        elif fat_chicken == 3:
            turnon.adjust_angle(50)
    elif angle == "6":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(29)
        elif fat_chicken == 3:
            turnon.adjust_angle(49)
    elif angle == "7":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(28)
        elif fat_chicken == 3:
            turnon.adjust_angle(48)
    elif angle == "10":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(20)
        elif fat_chicken == 3:
            turnon.adjust_angle(40)
    elif angle == "11":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(19)
        elif fat_chicken == 3:
            turnon.adjust_angle(39)
    elif angle == "12":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(18)
        elif fat_chicken == 3:
            turnon.adjust_angle(38)
    elif angle == "13":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(17)
        elif fat_chicken == 3:
            turnon.adjust_angle(37)
    elif angle == "14":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(16)
        elif fat_chicken == 3:
            turnon.adjust_angle(36)
    elif angle == "15":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(15)
        elif fat_chicken == 3:
            turnon.adjust_angle(35)
    elif angle == "16":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(14)
        elif fat_chicken == 3:
            turnon.adjust_angle(34)
    elif angle == "17":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(13)
        elif fat_chicken == 3:
            turnon.adjust_angle(33)
    elif angle == "19":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(11)
        elif fat_chicken == 3:
            turnon.adjust_angle(31)
    elif angle == "20":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(10)
        elif fat_chicken == 3:
            turnon.adjust_angle(30)
    elif angle == "21":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(9)
        elif fat_chicken == 3:
            turnon.adjust_angle(29)
    elif angle == "23":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(7)
        elif fat_chicken == 3:
            turnon.adjust_angle(27)
    elif angle == "25":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(5)
        elif fat_chicken == 3:
            turnon.adjust_angle(25)
    elif angle == "26":
        if fat_chicken == 1 or fat_chicken == 2:
            turnon.adjust_angle(4)
        elif fat_chicken == 3:
            turnon.adjust_angle(24)
    elif angle == "27" and fat_chicken == 3:
        turnon.adjust_angle(23)
    elif angle == "30" and fat_chicken == 3:
        turnon.adjust_angle(20)
    elif angle == "33" and fat_chicken == 3:
        turnon.adjust_angle(17)
    elif angle == "41" and fat_chicken == 3:
        turnon.adjust_angle(9)
    elif angle == "46" and fat_chicken == 3:
        turnon.adjust_angle(4)


def get_force(angle, fat_chicken):
    force = 3
    if angle == "41" or angle == "46":
        if fat_chicken == 1:
            force = 1.5
        elif fat_chicken == 2:
            force = 2.2
        elif fat_chicken == 3:
            force = 3
    elif angle == "50" or angle == "51":
        if fat_chicken == 1:
            force = 1.5
        elif fat_chicken == 2:
            force = 2.2
        elif fat_chicken == 3:
            force = 2.4
    else:
        if fat_chicken == 1:
            force = 2.1
        elif fat_chicken == 2:
            force = 3
        elif fat_chicken == 2:
            force = 2.4
    return force
