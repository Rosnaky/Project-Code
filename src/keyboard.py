from pynput.keyboard import Key, Listener, Controller
from threading import Thread

global terminate
terminate = False

keyboard = Controller()

def on_press(key):
    #print('{0} pressed'.format(
        #key))
    check_key(key)

def on_release(key):
    #print('{0} release'.format(
       # key))
    if key == Key.esc:
        # Stop listener
        return False

def check_key(key):
    if key == Key.ctrl:
        terminate = True

def listen():
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def pressKey_f11():
    keyboard.press(Key.f11)

def pressKey_esc():
    keyboard.press(Key.esc)


thread = Thread(target=listen)
