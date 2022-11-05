import zipfile as z
import time


def saveFile():
    while True:
        zip = z.ZipFile('files.zip', 'a')
        zip.write('logs.txt')
        zip.write('screenshots')
        zip.close()
        time.sleep(30)
