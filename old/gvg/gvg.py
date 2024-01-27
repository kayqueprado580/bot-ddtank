import time
import sys

from lib import fn_complement
from lib import turn_on
from lib import setting_room
from lib import mission

END_GAME = "img/end_game.png"
CARDS = "img/cards.png"
TOTAL = "img/total.png"
RESULT_TIME = "img/result_time.png"

walking_flag = True
attack_flag = True
changed_bool = False
my_turn = False
my_turn_option_attack = 0
count_pass = 0
is_end_game = False


def set_up_my_turn():
    global my_turn_option_attack
    print("Deseja passar ou apenas morrer ?")
    print("Tecle: ")
    print("1 - Passar || 2 - Morrer")
    input_user = input("Digite um 1, 2: ")
    try:
        my_turn_option_attack = int(input_user)
        if my_turn_option_attack == 1 or my_turn_option_attack == 2:
            if my_turn_option_attack == 1:
                print("selecionado passar...")
            else:
                print("selecionado morrer...")
        else:
            print("Erro: Por favor, digite apenas 1 ou 2")
            sys.exit()

    except ValueError:
        print("Erro: Por favor, digite um valor inteiro válido.")
        sys.exit()


def manager_attack(trident=False):
    if trident:
        turn_on.use_skills_trident()
    else:
        turn_on.use_skills_attack()
    turn_on.attack(0.05)
    time.sleep(6)


def manager_walking(right=False):
    if right:
        turn_on.walking_right()
        turn_on.change_side(0)
    else:
        turn_on.walking_left()
        turn_on.change_side(1)


def manager_pass(x, y):
    global count_pass
    turn_on.pass_turn(x, y)
    count_pass += 1
    time.sleep(1)


def manager_end_game():
    global walking_flag, attack_flag, changed_bool, count_pass, is_end_game
    end_game = fn_complement.find(END_GAME)
    cards = fn_complement.find(CARDS)
    if cards["found"] or end_game["found"]:
        is_end_game = True
        walking_flag = True
        attack_flag = True
        changed_bool = False
        count_pass = 0
        time.sleep(5)
        mission_accomplished = mission.found()
        if mission_accomplished:
            mission.completed()
            time.sleep(1)
            mission.collect()
            time.sleep(1.5)
            mission.close()
    else:
        is_end_game = False


def reset_default_parameters():
    global walking_flag, attack_flag, changed_bool, count_pass, is_end_game
    is_end_game = True
    walking_flag = True
    attack_flag = True
    changed_bool = False
    count_pass = 0


def manager_missions():
    mission_accomplished = mission.found()
    if mission_accomplished:
        mission.completed()
        time.sleep(1)
        mission.collect()
        time.sleep(1.5)
        mission.close()


set_up_my_turn()
while True:
    if setting_room.start_click:
        reset_default_parameters()
        manager_missions()
        setting_room.start_click = False
        time.sleep(2)
    if not my_turn:
        manager_end_game()
        if not is_end_game:
            setting_room.set_up(GVG=True)

    for img_pass in turn_on.IMAGES_PASS:
        turn = fn_complement.find(img_pass)
        if turn["found"]:
            my_turn = True
            if count_pass > 4:
                turn_on.click_for_attack(turn["position_x"], turn["position_y"])
            if changed_bool:
                walking_flag = not walking_flag
                attack_flag = not attack_flag
                changed_bool = False

            if my_turn_option_attack == 1:
                if count_pass < 10:
                    manager_pass(turn["position_x"], turn["position_y"])
                else:
                    changed_bool = True
                    manager_walking(walking_flag)
                    manager_attack(True)
            else:
                if count_pass < 6:
                    manager_pass(turn["position_x"], turn["position_y"])
                elif count_pass > 6 and count_pass < 10:
                    changed_bool = True
                    attack_flag = False
                    manager_walking(walking_flag)
                    manager_attack(True)
                else:
                    changed_bool = True
                    manager_walking(walking_flag)
                    manager_attack(True)
        else:
            my_turn = False

    time.sleep(0.3)
