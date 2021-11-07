import random
import time
import keyboard
from pynput.keyboard import Key, Controller

kb = Controller()


while True:
    print("press space to continue")
    keyboard.wait("space")

    try:
        while True:
            wait = random.uniform(2, 4)
            time.sleep(wait)
            kb.press(Key.ctrl)
            kb.press("e")
            kb.release("e")
            kb.release(Key.ctrl)
            print("sleep for ", wait)
    except KeyboardInterrupt:
        print("\n")
