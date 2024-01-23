import time
from lib import fn_complement

ROOM = "img/room.png"
PLAY = "img/play.png"
WAIT = "img/wait.png"
READY = "img/ready.png"
OK = "img/ok.png"
START = "img/btn_init.png"
AVAILABLE = "img/available.png"
BATTLE_FREE = "img/free_combat.png"


def set_up(GVG=False):
    global ROOM, PLAY, WAIT, READY, OK, START, AVAILABLE
    slot_available = True
    click_battle_free = False

    if GVG:
        slot_available = False
        click_battle_free = True

    if not click_battle_free:
        room = fn_complement.find(ROOM)
        if room["found"]:
            fn_complement.click("room", room["position_x"], room["position_y"])
            time.sleep(0.5)

        play = fn_complement.find(PLAY)
        if play["found"]:
            fn_complement.click(
                "enter the room", play["position_x"], play["position_y"]
            )
            time.sleep(0.5)
    if not GVG:
        slot = fn_complement.find(AVAILABLE)
        if slot["found"]:
            slot_available = True
            click_battle_free = False
            fn_complement.click("available", slot["position_x"], slot["position_y"])
        else:
            slot_available = False

    if not slot_available:
        if not click_battle_free and not GVG:
            battle = fn_complement.find(BATTLE_FREE)
            if battle["found"]:
                fn_complement.click(
                    "battle free", battle["position_x"], battle["position_y"]
                )
                click_battle_free = True

        if click_battle_free:
            ok = fn_complement.find(OK)
            if ok["found"]:
                fn_complement.click("ok", ok["position_x"], ok["position_y"])

            start = fn_complement.find(START)
            if start["found"]:
                fn_complement.click("start", start["position_x"], start["position_y"])
                time.sleep(5)
                click_battle_free = False

            wait = fn_complement.find(WAIT)
            if wait["found"]:
                fn_complement.click("wait", wait["position_x"], wait["position_y"])
                time.sleep(5)
