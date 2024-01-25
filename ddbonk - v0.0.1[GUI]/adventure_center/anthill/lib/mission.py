import time
from lib import fn_complement

QUEST = ["img/quest.png", "img/quest_1.png"]
COMPLETED = ["img/ok_mission.png", "img/ok_mission_1.png", "img/ok_mission_2.png"]
COLLECT_REWARD = "img/collect_reward.png"
CLOSE = "img/close.png"


def found():
    global QUEST
    rewards = False
    for img_quest in QUEST:
        quest = fn_complement.find(img_quest)
        if quest["found"]:
            fn_complement.click(
                "step: mission notified", quest["position_x"], quest["position_y"]
            )
            time.sleep(0.2)
            rewards = True
            break
    return rewards


def close():
    global CLOSE
    close = fn_complement.find(CLOSE)
    if close["found"]:
        fn_complement.click(
            "step: close mission", close["position_x"], close["position_y"]
        )


def completed():
    global COMPLETED
    i = 0
    while i < 5:
        for img_completed in COMPLETED:
            completed = fn_complement.find(img_completed)
            if completed["found"]:
                fn_complement.click(
                    "step: completed mission",
                    completed["position_x"],
                    completed["position_y"],
                )
                time.sleep(0.2)
                collect()
        i += 1


def collect():
    global COLLECT_REWARD
    collect = fn_complement.find(COLLECT_REWARD)
    if collect["found"]:
        fn_complement.click(
            "step: collect mission",
            collect["position_x"],
            collect["position_y"],
        )
        time.sleep(0.2)
