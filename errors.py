from search import searchUntilClick
from map import backToMap
import pyautogui
import time
import os
from logger import getLogger

logger = getLogger()


def checkNewErrors():
    error = pyautogui.locateOnScreen("images/ok.png")
    if(error is not None):
        logger.info("Refreshing browser...")
        pyautogui.hotkey("ctrl", "f5")
        time.sleep(5)
        searchUntilClick(["connect_wallet.png", "metamask.png", "sign.png"])
        time.sleep(5)
        if(not pyautogui.locateOnScreen("images/ok.png")):
            backToMap()
        else:
            time.sleep(int(os.getenv("REFRESH_BROWSER_COOLDOWN_MINUTES") * 60))
            checkNewErrors()
