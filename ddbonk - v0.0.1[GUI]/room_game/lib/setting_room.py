import time

# from lib import fn_complement
from fn_complement import *

ROOM = "../img/room.png"
PLAY = "../img/play.png"
WAIT = "../img/wait.png"
READY = "../img/ready.png"
OK = "../img/ok.png"
START = "../img/btn_init.png"
AVAILABLE = "../img/available.png"
BATTLE_FREE = "../img/free_combat.png"


def set_up(GVG=False):
    global ROOM, PLAY, WAIT, READY, OK, START, AVAILABLE
    slot_available = True
    click_battle_free = False

    if GVG:
        slot_available = False
        click_battle_free = True

    if not click_battle_free:
        room = find(ROOM)
        if room["found"]:
            click("room", room["position_x"], room["position_y"])
            time.sleep(0.5)

        play = find(PLAY)
        if play["found"]:
            click("enter the room", play["position_x"], play["position_y"])
            time.sleep(0.5)
    if not GVG:
        slot = find(AVAILABLE)
        if slot["found"]:
            slot_available = True
            click_battle_free = False
            click("available", slot["position_x"], slot["position_y"])
        else:
            slot_available = False

    # if click_battle_free:
    ok = find(OK)
    if ok["found"]:
        click("ok", ok["position_x"], ok["position_y"])

    if not slot_available:
        if not click_battle_free and not GVG:
            battle = find(BATTLE_FREE)
            if battle["found"]:
                click("battle free", battle["position_x"], battle["position_y"])
                click_battle_free = True

            start = find(START)
            if start["found"]:
                click("start", start["position_x"], start["position_y"])
                time.sleep(5)
                click_battle_free = False

            wait = find(WAIT)
            if wait["found"]:
                click("wait", wait["position_x"], wait["position_y"])
                time.sleep(5)
