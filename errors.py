from search import searchUntilClick
import pyautogui
import time
import os
from logger import getLogger
from action import solveCaptcha

logger = getLogger()


def checkNewErrors():
    if pyautogui.locateOnScreen("images/ok.png") is not None or pyautogui.locateOnScreen("images/ok_unstable.png"):
        logger.info("Refreshing browser...")
        pyautogui.hotkey("ctrl", "f5")
        time.sleep(10)
        searchUntilClick(["connect_wallet.png"])
        time.sleep(5)
        searchUntilClick(["sign.png"])
        time.sleep(20)
        searchUntilClick(["treasure_hunt.png"])
    else:
        pyautogui.click(100,100, clicks=2)
