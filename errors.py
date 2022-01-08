from search import searchUntilClick
import pyautogui
import time
import os
from logger import getLogger
from action import solveCaptcha

logger = getLogger()


def checkNewErrors():
    if(pyautogui.locateOnScreen("images/ok.png") is not None or pyautogui.locateOnScreen("images/connect_wallet.png")):
        logger.info("Refreshing browser...")
        pyautogui.hotkey("ctrl", "f5")
        time.sleep(10)
        searchUntilClick(["connect_wallet.png", "sign.png"])
        if(not pyautogui.locateOnScreen("images/ok.png")):
            searchUntilClick(["treasure_hunt.png"])
        else:
            time.sleep(int(os.getenv("REFRESH_BROWSER_COOLDOWN_MINUTES")) * 60)
            checkNewErrors()
    else:
        pyautogui.move(400, 400)
        pyautogui.click(500, 500)
