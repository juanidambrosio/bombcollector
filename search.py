import pyautogui
import time


def searchUntilClick(images):
    previousImage = None
    for val in images:
        t0 = time.time()
        imageNotFound = True
        print(val)
        while imageNotFound:
            t1 = time.time()
            if (t1 - t0 > 10 and previousImage is not None):
                pyautogui.click(previousImage)
                time.sleep(1)
            image = pyautogui.locateCenterOnScreen("images/" + val)
            if(image is not None):
                previousImage = image
                pyautogui.click(image, clicks=1)
                imageNotFound = False
