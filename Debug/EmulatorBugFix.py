from subprocess import Popen
from pywinauto import Desktop
import pywinauto.application
from pywinauto import Application
from pynput.keyboard import Key, Controller
import time
import threading

program_path = "C:\\Users\\Nate Hindman\\Desktop\\Emulators\\NES\\VirtuaNES.exe"
file_path    = "C:\\Users\\Nate Hindman\\Desktop\\Emulators\\NES\\NESROMS\\SuperMarioBrosDuckHunt.nes"
app = Application().start(r'{} "{}"'.format(program_path, file_path))
app = Application(backend='win32').connect(path=program_path)
keyboard = Controller()

def fixEmu(): #fix VirtuaNES keyboard bug
    pywinauto.mouse.click(button='left', coords=(960, 1080))
    app.top_window().set_focus()

def StartMenu(): #get past the start menu
    
      for x in range(0,3): # press enter twice
          keyboard.press('l')
          fixEmu()
def TXTintoDLL():
    pass
      
def PlaybackPress():
    StartMenu()
    for length in range(0,100):   
        keyboard.press('x')
        fixEmu()

if __name__ == "__main__":

    time.sleep(5)
    t1 = threading.Thread(target=PlaybackPress) 
    t1.start()
