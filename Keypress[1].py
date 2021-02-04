from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def KeyboardDemo():
    for x in range(0,1000):
        time.sleep(0.2)
        keyboard.press('f')
        print(x)
        


if __name__ == "__main__":
    KeyboardDemo()
