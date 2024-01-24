import time
from lib import fn_complement

CENTRAL = "img/central.png"
PLAY = "img/play.png"
READY = "img/ready.png"
OK = "img/ok.png"
START = "img/start.png"
AVAILABLE = "img/available.png"
CHECK_STAGE_1 = "img/check.png"
CHECK_STAGE_2 = "img/pandora/stage_2.png"
SELECTED_ANT = "img/selected_ant.png"
SELECT = "img/select.png"
CLOSE = "img/close.png"
LEVELS = [
    {"key": "easy", "path": "img/easy.png"},
    {"key": "normal", "path": "img/normal.png"},
]


def set_up(level):
    global CENTRAL, PLAY, READY, OK, START, AVAILABLE
    slot_available = True
    selected_ant = False
    enable_start = False
    stage = 1

    if check_stage_1():
        stage = 1
        slot_available = False
        selected_ant = True
        enable_start = True

    if check_stage_2():
        stage = 2
        slot_available = False
        selected_ant = True
        enable_start = True

    central = fn_complement.find(CENTRAL)
    if central["found"]:
        fn_complement.click("central", central["position_x"], central["position_y"])
        time.sleep(0.5)

    play = fn_complement.find(PLAY)
    if play["found"]:
        fn_complement.click("enter the room", play["position_x"], play["position_y"])
        time.sleep(0.5)

    slot = fn_complement.find(AVAILABLE)
    if slot["found"]:
        slot_available = True
        fn_complement.click("available", slot["position_x"], slot["position_y"])
    else:
        slot_available = False

    if not slot_available:
        ok = fn_complement.find(OK)
        if ok["found"]:
            fn_complement.click("ok", ok["position_x"], ok["position_y"])
            enable_start = True
            time.sleep(0.5)

        if not enable_start:
            select = fn_complement.find(SELECT)
            if select["found"]:
                fn_complement.click(
                    "select", select["position_x"], select["position_y"]
                )
                time.sleep(0.5)

            selected = fn_complement.find(SELECTED_ANT)
            if selected["found"]:
                fn_complement.click(
                    "select", selected["position_x"], selected["position_y"]
                )
                selected_ant = True
                time.sleep(0.5)

            if selected_ant:
                lvl = fn_complement.find(LEVELS[level - 1]["path"])
                if lvl["found"]:
                    fn_complement.click(
                        LEVELS[level - 1]["key"], lvl["position_x"], lvl["position_y"]
                    )
                    time.sleep(0.5)

        if enable_start:
            start = fn_complement.find(START)
            if start["found"]:
                fn_complement.click("start", start["position_x"], start["position_y"])
                time.sleep(1)
    return stage


def check_stage_1():
    global CHECK_STAGE_1
    found = False
    check = fn_complement.find(CHECK_STAGE_1, use_gray=True)
    if check["found"]:
        found = True
        print(f"step: check stage 1")
    return found


def check_stage_2():
    global CHECK_STAGE_2
    found = False
    check = fn_complement.find(CHECK_STAGE_2, use_gray=True)
    if check["found"]:
        found = True
        print(f"step: check stage 2")
    return found
