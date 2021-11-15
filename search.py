import pyautogui
import time
from logger import getLogger

logger = getLogger()


def searchUntilClick(images):
    for val in images:
        print(val)
        retries = 0
        while (image := pyautogui.locateOnScreen("images/" + val)) is not None or retries < 3:
            if(image is not None):
                pyautogui.leftClick(image, duration=0.75)
                pyautogui.moveTo(image.left - 100, image.top - 100)
                time.sleep(1)
            retries += 1


def locateAnyEmptyChest():
    i = 0
    while i < 3:
        if (pyautogui.locateOnScreen("images/blue1.png") is not None or
            pyautogui.locateOnScreen("images/blue2.png") or
            pyautogui.locateOnScreen("images/yellow1.png") is not None or
            pyautogui.locateOnScreen("images/yellow2.png") or
            pyautogui.locateOnScreen("images/violet1.png") is not None or
                pyautogui.locateOnScreen("images/violet2.png")):
            logger.info("Found empty chest")
            return True
    else:
        i += 1
    return False
