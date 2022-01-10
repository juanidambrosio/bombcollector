import pyautogui
import time
from search import searchUntilClick
from logger import getLogger
from action import changeWorkersState, solveCaptcha

logger = getLogger()


def putHeroesToWork():

    treasureHunt = pyautogui.locateOnScreen("images/treasure_hunt.png")
    if (treasureHunt is not None):
        pyautogui.click(treasureHunt)
        time.sleep(5)
    searchUntilClick(["back_to_main_menu.png", "heroes.png"])
    all = pyautogui.locateOnScreen("images/all.png")
    print("Enabled workers")
    if (all is not None):
        pyautogui.click(all, clicks=2)
    # enableWorkers()
    searchUntilClick(["back_to_main_menu_2.png", "treasure_hunt.png"])
    logger.info("Completed enabling workers")


# def enableWorkers(enableBestHeroes):
#     workEnabledFound = True
#     pyautogui.moveTo(700, 800)
#     pyautogui.mouseDown(button="left")
#     pyautogui.dragTo(700, 200, 0.5, button="left")
#     pyautogui.mouseUp(button="left")
#     time.sleep(5)
#     heroeTypes = ["common"]
#     if(enableBestHeroes):
#         heroeTypes = heroeTypes + ["rare", "superrare"]
#     while workEnabledFound:
#         logger.info("Enabling workers...")
#         pyautogui.click(500,500)
#         result = changeWorkersState("images/work.png", heroeTypes, False)
#         if(result == 0):
#             workEnabledFound = False
#         else:
#             time.sleep(1)



def enableOnlySuperHeroes():
    searchUntilClick(["back_to_main_menu.png", "heroes.png"])
    solveCaptcha()
    enableWorkers(True)
    pyautogui.moveTo(700, 400)
    time.sleep(2)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(700, 1000, 0.5, button="left")
    pyautogui.mouseUp(button="left")
    time.sleep(5)
    commonToRestFound = True
    while commonToRestFound:
        logger.info("Putting workers to rest...")
        result = changeWorkersState("images/rest.png", ["common"], True)
        if(result == 0):
            commonToRestFound = False
        else:
            time.sleep(1)
    searchUntilClick(["back_to_main_menu_2.png", "treasure_hunt.png"])
    logger.info("Enabled super heroes!")
