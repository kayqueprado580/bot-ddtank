import time
import sys

from lib import turn_on
from lib import fn_complement
from lib import setting_instance
from lib import mission
from stage_1 import set_default_parameters_ants, turn_on_ants_stage_1
from stage_2 import reset_parameters_default, turn_on_boss_stage_2

END_GAME = "img/end_game.png"
CARDS = "img/cards.png"
WIN = "img/win_stage_2.png"


def set_up_level():
    level = 1

    print("Selecione o nível...")
    print("Tecle: ")
    print("1 - Facil ou 2 - Normal")
    input_user = input("Digite um 1 ou 2: ")

    try:
        level = int(input_user)
        if level == 1 or level == 2:
            print("Level selecionado: ")
            if level == 1:
                print("Facil")
            else:
                print("Normal")
        else:
            print("Erro: Por favor, digite apenas 1 ou 2.")
            sys.exit()

    except ValueError:
        print("Erro: Por favor, digite um valor inteiro válido.")
        sys.exit()

    return level


def manager_end_game():
    global is_end_game, my_turn
    end_game = fn_complement.find(END_GAME)
    cards = fn_complement.find(CARDS)
    win = fn_complement.find(WIN)
    if cards["found"] or end_game["found"] or win["found"]:
        print("step: end game")
        is_end_game = True
        my_turn = False
        stage = 1
        time.sleep(5)
        reset_parameters_default()
        set_default_parameters_ants()
        mission_accomplished = mission.found()
        if mission_accomplished:
            mission.completed()
            time.sleep(1)
            mission.collect()
            time.sleep(1.5)
            mission.close()
    else:
        is_end_game = False


is_end_game = False
my_turn = False
stage = 1
count = 0
level = set_up_level()
while True:
    if not my_turn:
        manager_end_game()
        if setting_instance.selected_ant:
            stage = 1
        if setting_instance.check_stage_1():
            stage = 1
            print("step: stage 1")
            reset_parameters_default()
            set_default_parameters_ants()
        if setting_instance.check_stage_2():
            stage = 2
            print("step: stage 2")
            set_default_parameters_ants()

        if not is_end_game:
            setting_instance.set_up(level)

    for img_pass in turn_on.IMAGES_PASS:
        turn = fn_complement.find(img_pass)
        if turn["found"]:
            setting_instance.reset_set_up()
            setting_instance.selected_ant = False
            my_turn = True
            print(f"stage: {stage}")
            if count < 1:
                turn_on.click_for_attack(turn["position_x"], turn["position_y"])
            if stage == 1:
                turn_on_ants_stage_1()
            else:
                turn_on_boss_stage_2()

        else:
            my_turn = False
    if count >= 3:
        count = 0
    else:
        count += 1
    time.sleep(0.2)
