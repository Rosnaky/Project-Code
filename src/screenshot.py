# set display to 0
import os 
os.environ['DISPLAY'] = ':0'

from PIL import ImageGrab
import pyautogui
from screeninfo import get_monitors, Monitor
import keyboard
import time 

"""
Dependencies:
- pip install pillow
- pip install pyautogui
- pip install screeninfo
- pip install keyboard
"""
WIDTH = 1024
HEIGHT = 768
X_POSITION = 10
Y_POSITION = 10

def getScreenshots(code_file_path, images_dir_path, MAX_ELAPSED_TIME=60):
    # get size of screen
    
    monitor = Monitor(
        x=X_POSITION,
        y=Y_POSITION,
        width=WIDTH,
        height=HEIGHT
    )

    width = monitor.width
    height = monitor.height

    def scroll(height):
        pyautogui.scroll(height)

    os.system("export DISPLAY=:0")
    # * Enable on prod
    # os.system("sudo pkill -f code")
    os.system(f"code {code_file_path}")
    
    # Enter full screen
    keyboard.pressKey_esc()
    keyboard.pressKey_f11()

    time.sleep(10)
    start_time = time.time()


    def image_to_bytes(image):
        return list(image.getdata())

    count = 0
    prev_screenshot = None


    while time.time() - start_time < MAX_ELAPSED_TIME:
        
        if (keyboard.terminate):
            break

        # take screenshot 
        screenshot = ImageGrab.grab(bbox =(0, 0, width, height))
        
        # if the two screenshots are the same that means we've reached the end of our scrollable area 
        if image_to_bytes(screenshot) == prev_screenshot:
            break

        prev_screenshot = image_to_bytes(screenshot)
        img_path = os.path.join(images_dir_path, f"pic {count}.png")
        
        screenshot.save(img_path)
        scroll(-height)
        count += 1
        time.sleep(0.5)

# below is an example call of the function
# screenshotCapture("C:\\Users\\haris\\OneDrive\\Desktop\\SE101\\se101-f2024-triangles\\triangle.c")
