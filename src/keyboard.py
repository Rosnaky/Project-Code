import pynput
# from pynput.keyboard import Key, Listener, Controller
from threading import Thread
import time

class Keyboard:

    def __init__(self):
        self.terminate = False
        self.keyboard = pynput.keyboard.Controller()
        self.mouse = pynput.mouse.Controller()

        thread = Thread(target=self.listen)

    def on_press(self, key):
        #print('{0} pressed'.format(
            #key))
        self.check_key(key)

    def on_release(self, key):
        #print('{0} release'.format(
        # key))
        if key == pynput.keyboard.Key.esc:
            # Stop listener
            return False

    def check_key(self, key):
        if key == pynput.keyboard.Key.ctrl:
            terminate = True

    def listen(self):
        # Collect events until released
        with pynput.keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def pressKey_f11(self):
        self.keyboard.tap(pynput.keyboard.Key.f11)

    def pressKey_esc(self):
        self.keyboard.tap(pynput.keyboard.Key.esc)

    def scroll(self, x, y):
        self.mouse.scroll(x, y)

    def left_click(self):
        self.mouse.click(pynput.mouse.Button.left)

