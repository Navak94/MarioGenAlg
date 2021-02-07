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

exec(open("Record.py").read())
