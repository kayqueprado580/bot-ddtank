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
attack_left = False
attack_right = False
force = 0.8


def set_default_parameters_ants():
    global count_turn_right, count_turn_left, turn_count, fly_used, attack_right, attack_left, force
    force = 0.8
    count_turn_right = 0
    count_turn_left = 0
    turn_count = 0
    fly_used = False
    attack_left = False
    attack_right = False


def look_ants_left():
    global IMAGES_ANTS_LEFT
    monster_found = False
    for img_left in IMAGES_ANTS_LEFT:
        ants_left = fn_complement.find(img_left["path"])
        if ants_left["found"]:
            print("step: monsters on the left")
            monster_found = True
            break
    return monster_found


def look_ants_right():
    global IMAGES_ANTS_RIGHT
    monster_found = False
    for img_right in IMAGES_ANTS_RIGHT:
        ants = fn_complement.find(img_right["path"])
        if ants["found"]:
            print("step: monsters on the right")
            monster_found = True
            break
    return monster_found


def define_force():
    global fly_used, turn_count, force
    if not fly_used:
        if turn_count == 1:
            force = 0.9
        elif turn_count == 2:
            force = 0.8
        elif turn_count > 2 and turn_count <= 4:
            force = 0.7
        elif turn_count > 4 and turn_count <= 6:
            force = 0.6
        else:
            force = 0.45
    else:
        if turn_count == 1:
            force = 1
        elif turn_count == 2:
            force = 0.8
        elif turn_count > 2 and turn_count <= 4:
            force = 0.6
        elif turn_count > 4 and turn_count <= 6:
            force = 0.5
        else:
            force = 0.4


def turn_on_ants_stage_1():
    global attack_left, attack_right, count_turn_right, count_turn_left
    global turn_count, fly_used, MAX_SIDE_TURN, MAX_TURN_COUNT, force

    print(f"step: my turn - count turn: {turn_count} / {MAX_TURN_COUNT}")
    if turn_count >= MAX_TURN_COUNT and not fly_used:
        print("step: my turn - max turn enabled fly")
        fly_used = True
        turn_on.use_fly()
        time.sleep(0.5)
    elif turn_count >= MAX_TURN_COUNT and fly_used:
        print("step: my turn - max turn and fly used, changed side")
        if attack_left:
            turn_on.change_side(0)
            turn_on.walking_right()
        if attack_right:
            turn_on.change_side(1)
            turn_on.walking_left()
        turn_count = 0
    else:
        define_force()
        found_left = look_ants_left()
        if found_left:
            attack_left = True
            attack_right = False
            if not fly_used:
                if count_turn_left >= MAX_SIDE_TURN:
                    print("step: my turn - max turn left - changed side...")
                    turn_on.walking_right()
                    count_turn_left = 0
                else:
                    turn_on.walking_left()
                    count_turn_left += 1
                    print(
                        f"step: my turn - count turn left: {count_turn_left} / {MAX_SIDE_TURN}"
                    )
        if not found_left:
            found_right = look_ants_right()
            if found_right:
                attack_left = False
                attack_right = True
                if not fly_used:
                    if count_turn_right >= MAX_SIDE_TURN:
                        print("step: my turn - max turn right - changed side...")
                        turn_on.walking_left()
                        count_turn_right = 0
                    else:
                        turn_on.walking_right()
                        count_turn_right += 1
                        print(
                            f"step: my turn - count turn right: {count_turn_right} / {MAX_SIDE_TURN}"
                        )
        print(f"step: my turn - force: {force}")
        turn_on.use_skills_trident()
        turn_on.attack(force)
        turn_count += 1
        time.sleep(6)
