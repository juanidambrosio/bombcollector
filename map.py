import pyautogui
from logger import getLogger

logger = getLogger()


def checkNewMap():
    newMap = pyautogui.locateOnScreen("images/new_map.png")
    if(newMap is not None):
        pyautogui.click(newMap)
        logger.info("New map unlocked!")


def backToMap():
    while(not pyautogui.locateOnScreen("images/back_to_main_menu.png")):
        pyautogui.click(pyautogui.locateOnScreen("images/treasure_hunt.png"))
