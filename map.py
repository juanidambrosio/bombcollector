import pyautogui
from logger import getLogger
import work
import time

logger = getLogger()


def checkNewMap():
    newMap = pyautogui.locateOnScreen("images/new_map.png")
    if(newMap is not None):
        pyautogui.click(newMap, clicks=2)
        logger.info("New map unlocked!")
        time.sleep(5)
        work.enableOnlySuperHeroes()
