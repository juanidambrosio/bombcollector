import pyautogui
import time
from logger import getLogger

logger = getLogger()


# def changeWorkersState(actionImage, heroeTypes, reverse):
#     actionButtons = list(pyautogui.locateAllOnScreen(actionImage))
#     if (reverse == True):
#         actionButtons = actionButtons[::-1]
#     for button in actionButtons:
#         pyautogui.leftClick(button.left - 100, button.top, duration=0.5)
#         time.sleep(1)
#         for heroeType in heroeTypes:
#             if(pyautogui.locateOnScreen("images/" + heroeType + ".png")):
#                 logger.info("Changing " + heroeType + "heroe state")
#                 pyautogui.leftClick(button, duration=0.25)
#     return len(actionButtons)

def changeWorkersState(actionImage):
    pyautogui.leftClick(actionImage, duration=0.5)
    time.sleep(1)
    
def solveCaptcha():
    # slide = pyautogui.locateOnScreen("images/captchaSlide.png")
    # retries = 0
    # missingPiece = None
    # while(retries < 10 and missingPiece is None):
    #     missingPiece = pyautogui.locateOnScreen("images/captcha.png")
    # logger.info(slide)
    # logger.info(missingPiece)
    # if(slide is not None and missingPiece is not None):
    #     pyautogui.moveTo(slide)
    #     pyautogui.mouseDown(button="left")
    #     pyautogui.dragTo(missingPiece.left, slide.top, button="left")
    #     pyautogui.mouseUp(button="left")
    return