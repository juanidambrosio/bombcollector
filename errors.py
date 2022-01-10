from search import searchUntilClick
import pyautogui
import time
import os
from logger import getLogger
from action import solveCaptcha

logger = getLogger()


def checkNewErrors():
    if pyautogui.locateOnScreen("images/ok.png") is not None:
        logger.info("Refreshing browser...")
        pyautogui.hotkey("ctrl", "f5")
        time.sleep(10)
        searchUntilClick(["connect_wallet.png"])
        time.sleep(5)
        searchUntilClick(["sign.png"])
        time.sleep(20)
        searchUntilClick(["treasure_hunt.png"])
