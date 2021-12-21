from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def KeyboardDemo():
    for x in range(0,1000):
        if x==1 or x ==2:
            time.sleep(1)
            keyboard.press(Key.enter)
        time.sleep(0.2)
        keyboard.press('x')
        print(x)
        


if __name__ == "__main__":
    KeyboardDemo()
