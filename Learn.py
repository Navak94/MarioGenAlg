from subprocess import Popen
from pywinauto import Desktop
import pywinauto.application
from pywinauto import Application
from pynput.keyboard import Key, Controller
import time
import threading
from numpy import loadtxt
import cv2
import numpy as np
import pytesseract
import time
from PIL import Image, ImageGrab , ImageOps

program_path = "C:\\Users\\Nate Hindman\\Desktop\\Emulators\\NES\\VirtuaNES.exe"
file_path    = "C:\\Users\\Nate Hindman\\Desktop\\Emulators\\NES\\NESROMS\\SuperMarioBrosDuckHunt.nes"
app = Application().start(r'{} "{}"'.format(program_path, file_path))
app = Application(backend='win32').connect(path=program_path)
keyboard = Controller()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def fixEmu(): #fix VirtuaNES keyboard bug
    pywinauto.mouse.click(button='left', coords=(960, 1080))
    app.top_window().set_focus()

def AvailableBtn():
    pass

def btnpress():
    keyboard.press('l')
    fixEmu()


def failureThreshold():
    
    while 1:
       
        x = 648
        y = 549
        offx = 649
        offy = 80

        img = ImageGrab.grab(bbox=(x,y,x + offx , y+ offy))


        img = ImageOps.invert(img) # since tesseract is trained for white background with black text this inverts the selection to correct the input.


        img = np.array(img)

        #cv2.imshow('window',img)
        # Just for debugging, gives you a snapshot of what you're feeding tessetact
    
        text = pytesseract.image_to_string(img)

        #print(text)

        if 'GAME' in text:
            print('GAME OVER')
        else:
            pass

        if 'TIME' in text:
            print('TIME')
        else:
            pass

    
def EpochGen():
    pass

if __name__ == "__main__":
    #time.sleep(410)
    t1 = threading.Thread(target=failureThreshold) 
    t1.start()

    
