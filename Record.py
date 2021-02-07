import xlwt
from pynput import keyboard
from pynput import mouse

def on_press(key):
    try:
        text_file = open("C:\\Users\\Nate Hindman\\Desktop\\Emulators\\NES\\MarioNN\\logs\\Output.txt", "a")
        text_file.write('{0}'.format(key.char))
        text_file.close()
    except AttributeError:
        text_file = open("Output.txt", "a")
        text_file.close()

def on_release(key):    
    if key == keyboard.Key.esc:      
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
