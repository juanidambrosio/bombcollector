import pyautogui
import time
from search import searchUntilClick, locateAnyEmptyChest
from logger import getLogger
from action import changeWorkersState

logger = getLogger()


def putHeroesToWork():

    treasureHunt = pyautogui.locateOnScreen("images/treasure_hunt.png")
    enableBestHeroes = True
    if (treasureHunt is not None):
        pyautogui.click(treasureHunt)
        if (locateAnyEmptyChest()):
            enableBestHeroes = False
    searchUntilClick(["back_to_main_menu.png", "heroes.png"])
    logger.info("Entered to workers panel")
    time.sleep(2)
    enableWorkers(enableBestHeroes)
    searchUntilClick(["back_to_main_menu_2.png", "treasure_hunt.png"])
    logger.info("Completed enabling workers")


def enableWorkers(enableBestHeroes):
    workEnabledFound = True
    pyautogui.moveTo(700, 800)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(700, 200, 0.5, button="left")
    pyautogui.mouseUp(button="left")
    time.sleep(5)
    while workEnabledFound:
        workButtons = list(pyautogui.locateAllOnScreen("images/work.png"))
        superHeroes = []
        if (not enableBestHeroes):
            superHeroes = list(
                pyautogui.locateAllOnScreen("images/superrare.png")) + list(pyautogui.locateAllOnScreen("images/rare.png"))
        length = len(workButtons)
        logger.info(f"Found {length} to enable")
        if length > 0 and len(superHeroes) < 5:
            for button in workButtons:
                superHero = any(heroe.top - button.top ==
                                18 for heroe in superHeroes)
                if (superHero == True):
                    logger.info("Avoided enabling super hero")
                else:
                    pyautogui.click(button)
                time.sleep(1)
        else:
            workEnabledFound = False


def enableOnlySuperHeroes():
    searchUntilClick(["back_to_main_menu.png", "heroes.png"])
    enableWorkers(True)
    pyautogui.moveTo(700, 400)
    time.sleep(1)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(700, 1000, 0.5, button="left")
    pyautogui.mouseUp(button="left")
    time.sleep(5)
    commonToRestFound = True
    while commonToRestFound:
        result = changeWorkersState("images/rest.png", ["images/common.png"], True)
        if(result == 0):
            commonToRestFound = False
        else:
            time.sleep(2)
    searchUntilClick(["back_to_main_menu_2.png", "treasure_hunt.png"])
    logger.info("Enabled super heroes!")
