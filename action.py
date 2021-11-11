import pyautogui
import time
from logger import getLogger

logger = getLogger()


def changeWorkersState(actionImage, heroeTypes, reverse):
    count = 0
    actionButtons = list(pyautogui.locateAllOnScreen(actionImage))
    if (reverse == True):
        actionButtons = actionButtons[::-1]
    for button in actionButtons:
        pyautogui.leftClick(button.left - 100, button.top, duration=0.5)
        time.sleep(1)
        for heroeType in heroeTypes:
            if(pyautogui.locateOnScreen(heroeType)):
                count += 1
                pyautogui.leftClick(button, duration=0.25)
    pyautogui.move(50, 0)
    return count
