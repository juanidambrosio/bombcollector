import pyautogui
import time
from search import searchUntilClick
from logger import getLogger

logger = getLogger()


def putHeroesToWork():
    treasureHunt = pyautogui.locateOnScreen("images/treasure_hunt.png")
    if(treasureHunt is not None):
        searchUntilClick(["heroes.png"])
    else:
        searchUntilClick(["back_to_main_menu.png", "heroes.png"])
    logger.info("Entered to workers panel")
    time.sleep(2)
    enableWorkers()
    searchUntilClick(["back_to_main_menu_2.png", "treasure_hunt.png"])


def enableWorkers():
    while(pyautogui.locateOnScreen("images/treasure_hunt.png")):
        heroes = pyautogui.locateOnScreen("images/heroes.png")
        pyautogui.click(heroes)
    workEnabledFound = True
    pyautogui.moveTo(700,800)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(700,200, 0.5, button="left")
    pyautogui.mouseUp(button="left")
    time.sleep(5)
    while workEnabledFound:
        workButtons = list(pyautogui.locateAllOnScreen("images/work.png"))
        length = len(workButtons)
        logger.info(f"Found {length} to enable")
        if len(workButtons) > 0:
            for button in workButtons:
                pyautogui.click(button)
                time.sleep(1)
        else:
            workEnabledFound = False
