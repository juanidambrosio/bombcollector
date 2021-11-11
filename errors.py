from search import searchUntilClick
import pyautogui
import time
import os
from logger import getLogger

logger = getLogger()


def checkNewErrors():
    if((pyautogui.locateOnScreen("images/ok.png") is not None or pyautogui.locateOnScreen("images/ok2.png") is not None)):
        logger.info("Refreshing browser...")
        pyautogui.hotkey("ctrl", "f5")
        time.sleep(5)
        searchUntilClick(["connect_wallet.png", "metamask.png", "sign.png"])
        time.sleep(5)
        if(not pyautogui.locateOnScreen("images/ok.png")):
            searchUntilClick(["treasure_hunt.png"])
        else:
            time.sleep(int(os.getenv("REFRESH_BROWSER_COOLDOWN_MINUTES") * 60))
            checkNewErrors()
