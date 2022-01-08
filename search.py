import pyautogui
import time
from logger import getLogger

logger = getLogger()


def searchUntilClick(images):
    for val in images:
        image = pyautogui.locateOnScreen("images/" + val)
        print(image)
        pyautogui.click(image, clicks=2)
        time.sleep(1)
