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

MAX_TURN = 20
MAX_TURN_PASS = 6
walking_flag = True
attack_flag = True
changed_bool = False
my_turn = False
my_turn_option_attack = 0
count_turn = 0
is_end_game = False


def set_up_default_parameters():
    global walking_flag, attack_flag, changed_bool, my_turn, count_turn
    walking_flag = True
    attack_flag = True
    changed_bool = False
    my_turn = False
    count_turn = 0


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
    turn_on.attack(0.03)
    time.sleep(7)


def manager_walking(right=False):
    if right:
        turn_on.walking_right()
        turn_on.change_side(0)
    else:
        turn_on.walking_left()
        turn_on.change_side(1)


def manager_pass(x, y):
    turn_on.pass_turn(x, y)
    time.sleep(2)


def option_pass(turn_x, turn_y):
    global MAX_TURN_PASS, count_turn, changed_bool, walking_flag
    max = MAX_TURN_PASS * 2
    if count_turn < max:
        manager_pass(turn_x, turn_y)
    else:
        changed_bool = True
        manager_walking(walking_flag)
        manager_attack(trident=True)


def option_attack(turn_x, turn_y):
    global MAX_TURN_PASS, count_turn, changed_bool, walking_flag
    if count_turn <= MAX_TURN_PASS:
        manager_pass(turn_x, turn_y)
    else:
        changed_bool = True
        manager_walking(walking_flag)
        manager_attack(trident=True)


def manager_missions():
    print("step: missions")
    mission_accomplished = mission.found()
    if mission_accomplished:
        mission.completed()
        time.sleep(1)
        mission.collect()
        time.sleep(1.5)
        mission.close()


def manager_end_game():
    global is_end_game
    global RESULT_TIME, END_GAME, TOTAL, CARDS
    result_time = fn_complement.find(RESULT_TIME)
    end_game = fn_complement.find(END_GAME)
    total = fn_complement.find(TOTAL)
    cards = fn_complement.find(CARDS)
    if cards["found"] or end_game["found"] or result_time["found"] or total["found"]:
        print("step: end game")
        is_end_game = True
        set_up_default_parameters()
        time.sleep(5)
        manager_missions()
    else:
        is_end_game = False


set_up_my_turn()

while True:
    if not my_turn:
        manager_end_game()
        if not is_end_game:
            setting_room.set_up(GVG=True)

    for img_pass in turn_on.IMAGES_PASS:
        turn = fn_complement.find(img_pass)
        if turn["found"]:
            my_turn = True
            time.sleep(0.5)
            if changed_bool:
                walking_flag = not walking_flag
                changed_bool = False
            if my_turn_option_attack == 1:
                option_pass(turn["position_x"], turn["position_y"])
            else:
                time.sleep(0.5)
                turn_on.click_for_attack(turn["position_x"], turn["position_y"])
                option_attack(turn["position_x"], turn["position_y"])

            if count_turn <= MAX_TURN:
                count_turn += 1
            else:
                count_turn = 0
            print(f"step: my turn - count turn: {count_turn} / {MAX_TURN}")
        else:
            my_turn = False

    time.sleep(0.3)
