import time

from lib import fn_complement
from lib import turn_on

IMAGES_ANTS_LEFT = [
    {"key": "ant_left", "path": "img/ants/ant_red_left.png"},
    {"key": "ant_left", "path": "img/ants/ant_red_left_1.png"},
    {"key": "ant_left", "path": "img/ants/ant_blue_left.png"},
    {"key": "ant_left", "path": "img/ants/ant_blue_left_1.png"},
    {"key": "ant_left", "path": "img/ants/ant_blue_left_2.png"},
]
IMAGES_ANTS_RIGHT = [
    {"key": "ant_right", "path": "img/ants/red_ant_right.png"},
    {"key": "ant_right", "path": "img/ants/ant_blue_right.png"},
    {"key": "ant_right", "path": "img/ants/ant_blue_right_1.png"},
]

# SETTINGS TURN
fly_used = False
count_turn_right = 0
count_turn_left = 0
turn_count = 0
MAX_SIDE_TURN = 5
MAX_TURN_COUNT = 10


def set_default_parameters_ants():
    global count_turn_right, count_turn_left, turn_count, fly_used
    count_turn_right = 0
    count_turn_left = 0
    turn_count = 0
    fly_used = False


def look_ants_left():
    global IMAGES_ANTS_LEFT
    monster_found = False
    for img_left in IMAGES_ANTS_LEFT:
        ants_left = fn_complement.find(img_left["path"], use_gray=True)
        if ants_left["found"]:
            print("monsters on the left")
            monster_found = True
            break
    return monster_found


def look_ants_right():
    global IMAGES_ANTS_RIGHT
    monster_found = False
    for img_right in IMAGES_ANTS_RIGHT:
        ants = fn_complement.find(img_right["path"], use_gray=True)
        if ants["found"]:
            print("monsters on the right")
            monster_found = True
            break
    return monster_found


def turn_on_ants_stage_1():
    global count_turn_right, count_turn_left, turn_count, fly_used, MAX_SIDE_TURN, MAX_TURN_COUNT

    attack_left = False
    attack_right = False

    force = 1
    if turn_count < 2:
        force = 0.7
    elif turn_count > 3 and turn_count <= 5:
        force = 0.6
    else:
        force = 0.5

    if turn_count > MAX_TURN_COUNT and fly_used:
        if attack_left:
            turn_on.change_side(0)
            turn_on.walking_right()
        if attack_right:
            turn_on.change_side(1)
            turn_on.walking_left()
        turn_count = 0

    if turn_count > MAX_TURN_COUNT and not fly_used:
        fly_used = True
        turn_on.use_fly()
        time.sleep(0.5)

    if turn_count < MAX_TURN_COUNT:
        found_left = look_ants_left()
        if found_left:
            attack_left = True
            attack_right = False
            if not fly_used:
                if count_turn_left > MAX_SIDE_TURN:
                    print("max turn left - changed side...")
                    turn_on.walking_right()
                    count_turn_left = 0
                else:
                    turn_on.walking_left()
            count_turn_left += 1
        found_right = look_ants_right()
        if found_right and not found_left:
            attack_left = False
            attack_right = True
            if not fly_used:
                if count_turn_right > MAX_SIDE_TURN:
                    print("max turn right - changed side...")
                    turn_on.walking_left()
                    count_turn_right = 0
                else:
                    turn_on.walking_right()
            count_turn_right += 1

        turn_on.use_skills_trident()
        turn_on.attack(force)
        turn_count += 1
        time.sleep(6)
