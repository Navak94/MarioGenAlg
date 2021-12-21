import cv2
import numpy as np
import pytesseract
import time
from PIL import Image, ImageGrab , ImageOps


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
x = 648
y = 549
offx = 649
offy = 80

while 1:
    #time.sleep(2)
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
        print('TIME UP')
    else:
        pass
