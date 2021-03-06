import pyautogui
import time
from logger import getLogger

logger = getLogger()


def searchUntilClick(images):
    for val in images:
        retries = 0
        found = False
        while retries < 3 and found is False:
            pyautogui.moveTo(300, 150)
            image = pyautogui.locateOnScreen("images/" + val)
            if image is not None:
                print(val)
                pyautogui.click(image, clicks=2, interval=0.5)
                time.sleep(1)
                found = True
            else:
                retries += 1
                if retries == 3:
                    print(val + " not found")
    pyautogui.moveTo(300, 150)
