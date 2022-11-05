import pyautogui
import time


def takeSs():
    i = 0
    while True:

        screenshots = pyautogui.screenshot()

        filepath = "screenshots/"+str(i)+".jpg"
        i = i+1

        screenshots.save(filepath)
        time.sleep(30)
