import pyautogui
import time
from search import searchUntilClick
from logger import getLogger

logger = getLogger()


def putHeroesToWork():
    treasureHunt = pyautogui.locateOnScreen("images/treasure_hunt.png")
    if(treasureHunt is not None):
        pyautogui.click(treasureHunt)
    searchUntilClick(["back_to_main_menu.png", "heroes.png"])
    logger.info("Entered to workers panel")
    time.sleep(2)
    enableWorkers()
    searchUntilClick(["back_to_main_menu_2.png", "treasure_hunt.png"])


def enableWorkers():
    pyautogui.moveTo(100, 100)
    while(pyautogui.locateOnScreen("images/treasure_hunt.png")):
        heroes = pyautogui.locateOnScreen("images/heroes.png")
        pyautogui.click(heroes)
    currentXScroll = 200
    currentYScroll = 200
    pyautogui.scroll(100, currentXScroll, currentYScroll)
    workEnabledFound = True
    while workEnabledFound:
        workButton = list(pyautogui.locateAllOnScreen("images/work.png"))
        length = len(workButton)
        logger.info(f"Found {length} to enable")
        if len(workButton) > 0:
            for button in workButton:
                pyautogui.click(button, clicks=2)
                currentYScroll += 50
                pyautogui.scroll(100, currentXScroll, currentYScroll)
                time.sleep(1)
        else:
            workEnabledFound = False
