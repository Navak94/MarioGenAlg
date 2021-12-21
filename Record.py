import xlwt
from pynput import keyboard
from pynput import mouse

def on_press(key):
        pass

def on_release(key):    
    try:
        text_file = open("C:\\Users\\Nate Hindman\\Desktop\\Emulators\\NES\\MarioNN\\logs\\Output.txt", "a")
        text_file.write('{0}'.format(key.char))
        text_file.close()
    except AttributeError:
        pass

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
